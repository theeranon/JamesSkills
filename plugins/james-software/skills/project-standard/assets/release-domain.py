#!/usr/bin/env python3
"""Assemble production as a hosting-domain tree. Never deploys or reads runtime secrets."""
import argparse,fnmatch,json,os,subprocess,tempfile,re,tarfile,io
from pathlib import Path,PurePosixPath

def run(*args,cwd=None,env=None,raw=False):
    return subprocess.check_output(list(args),cwd=cwd,env=env,text=not raw).strip() if not raw else subprocess.check_output(list(args),cwd=cwd,env=env)
def build(root,out):
    cfg=json.loads((root/'.release-layout.json').read_text())
    if cfg.get('web_root')!='public_html':raise RuntimeError('web_root must be public_html')
    entries={}
    def add(path,data,mode='100644'):
        p=PurePosixPath(path)
        if p.is_absolute() or '..' in p.parts:raise RuntimeError('Unsafe target path')
        if any(s in {'.git','ai-context','.claude','.github','node_modules'} or s=='.env' or s.startswith('.env.') for s in p.parts):raise RuntimeError('Source/secret path in payload: '+path)
        for preserved in cfg.get('preserve',[]):
            prefix=preserved.rstrip('/')
            if path==prefix or path.startswith(prefix+'/'):return
            if prefix.startswith(path+'/'):raise RuntimeError('Artifact file shadows preserved server directory')
        if any(fnmatch.fnmatch(path,g) for g in cfg.get('exclude',[])):return
        if re.search(rb'-----BEGIN (?:OPENSSH |RSA |EC )?PRIVATE KEY-----\r?\n[A-Za-z0-9+/=\r\n]{32,}-----END (?:OPENSSH |RSA |EC )?PRIVATE KEY-----',data):raise RuntimeError('Private key in payload')
        entries[path]=(data,mode)
    if cfg.get('baseline_commit'):
        ref=cfg['baseline_commit']
        for row in run('git','ls-tree','-rz',ref,cwd=root,raw=True).split(b'\0'):
            if not row:continue
            meta,name=row.split(b'\t',1);mode,kind,sha=meta.decode().split();name=name.decode()
            if kind!='blob' or mode not in {'100644','100755'}:raise RuntimeError('Unsupported baseline entry')
            add(name,run('git','cat-file','blob',sha,cwd=root,raw=True),mode)
    tracked=run('git','ls-tree','-rz','HEAD',cwd=root,raw=True).split(b'\0')
    for mapping in cfg.get('mappings',[]):
        src=mapping['source'].rstrip('/');dst=mapping['target'].rstrip('/')
        for row in tracked:
            if not row:continue
            meta,name=row.split(b'\t',1);name=name.decode()
            if name!=src and not name.startswith(src+'/'):continue
            mode,kind,sha=meta.decode().split()
            if kind!='blob' or mode not in {'100644','100755'}:raise RuntimeError('Unsupported source entry')
            tail=name[len(src):].lstrip('/');target=dst+('/'+tail if tail else '')
            add(target,run('git','cat-file','blob',sha,cwd=root,raw=True),mode)
    if cfg.get('builder'):
        relative=PurePosixPath(cfg['generated_root'])
        if relative.is_absolute() or '..' in relative.parts:raise RuntimeError('generated_root must stay inside isolated source')
        with tempfile.TemporaryDirectory(prefix='si-build-input-') as scratch:
            work=Path(scratch)
            archive=run('git','archive','HEAD',cwd=root,raw=True)
            with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
                for item in tar.getmembers():
                    member=PurePosixPath(item.name)
                    if member.is_absolute() or '..' in member.parts or item.issym() or item.islnk():raise RuntimeError('Unsafe builder input')
                tar.extractall(work)
            generated=work/str(relative)
            if generated.exists():raise RuntimeError('Generated output must not be tracked source')
            subprocess.run(cfg['builder'],cwd=work,check=True,stdout=subprocess.DEVNULL)
            if generated.is_symlink() or not generated.is_dir():raise RuntimeError('Invalid generated output')
            for p in generated.rglob('*'):
                if p.is_symlink():raise RuntimeError('Symlink in generated release')
                if p.is_file():add(str(p.relative_to(generated)),p.read_bytes())
    for name,text in cfg.get('generated_files',{}).items():add(name,text.encode())
    public=[p for p in entries if p.startswith('public_html/') and Path(p).name not in {'.gitkeep','.keep'}]
    if not public:raise RuntimeError('No substantive public_html payload; configure an actual app mapping')
    php_count=0
    for name,(data,mode) in entries.items():
        p=out/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data);p.chmod(0o755 if mode=='100755' else 0o644)
        if name.endswith('.php'):
            subprocess.run(['php','-l',str(p)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE);php_count+=1
    return cfg,entries,php_count

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--push',action='store_true');ap.add_argument('--out');args=ap.parse_args()
    root=Path(run('git','rev-parse','--show-toplevel')).resolve()
    if run('git','status','--porcelain','--untracked-files=no',cwd=root):raise RuntimeError('Commit tracked changes first')
    source=run('git','rev-parse','HEAD',cwd=root)
    with tempfile.TemporaryDirectory(prefix='si-domain-release-') as tmp:
        out=Path(tmp)/'payload';out.mkdir();cfg,entries,php_count=build(root,out)
        if args.out:
            import shutil
            target=Path(args.out)
            if target.exists():raise RuntimeError('--out must not exist')
            shutil.copytree(out,target)
        env={**os.environ,'GIT_INDEX_FILE':str(Path(tmp)/'index')}
        run('git','read-tree','--empty',cwd=root,env=env)
        for name,(_,mode) in sorted(entries.items()):
            blob=run('git','hash-object','-w',str(out/name),cwd=root)
            run('git','update-index','--add','--cacheinfo',mode,blob,name,cwd=root,env=env)
        tree=run('git','write-tree',cwd=root,env=env)
        report={'source':source,'tree':tree,'files':len(entries),'web_root':'public_html','php_lint':'pass' if php_count else 'not-applicable','php_files_checked':php_count,'runtime_ready':cfg.get('runtime_ready',False),'pushed':False,'deployed':False}
        if args.push:
            if not cfg.get('publication_approved',False):raise RuntimeError('Artifact publication is not approved; preview is still available')
            if run('git','branch','--show-current',cwd=root)!=cfg.get('source_branch','main'):raise RuntimeError('Not the configured source branch')
            subprocess.run(['git','fetch','--quiet','origin'],cwd=root,check=True)
            branch=run('git','branch','--show-current',cwd=root)
            remote=run('git','rev-parse','refs/remotes/origin/'+branch,cwd=root)
            if remote!=source:raise RuntimeError('Push source branch first; release refuses concurrent/stale source')
            refs=run('git','ls-remote','--heads','origin','refs/heads/production',cwd=root)
            parent=refs.split()[0] if refs else ''
            if parent:subprocess.run(['git','fetch','--quiet','origin',parent],cwd=root,check=True)
            if parent and run('git','rev-parse',parent+'^{tree}',cwd=root)==tree:report['production']=parent
            else:
                argv=['git','commit-tree',tree,'-m','Domain-root production from '+source]+(['-p',parent] if parent else [])
                commit=run(*argv,cwd=root)
                subprocess.run(['git','push','origin',commit+':refs/heads/production'],cwd=root,check=True)
                report['production']=commit;report['pushed']=True
            report['published']=True
        print(json.dumps(report))
if __name__=='__main__':main()
