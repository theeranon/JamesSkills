#!/usr/bin/env python3
"""Local RAG search over the AI SEO knowledge base (no dependencies).

Splits every knowledge/*.md and checklists/*.md file into chunks at `## ` headings,
then ranks chunks with BM25 (+ boosts for title/tags/heading matches).

Usage:
  python3 scripts/search.py "schema faq fact hub"            # top 6 chunks, full text
  python3 scripts/search.py "review platforms" -k 3
  python3 scripts/search.py "internal links" --list           # headings only
  python3 scripts/search.py --section "Audit checks"          # every chunk with that heading
Write queries in English (the knowledge base is English); translate Thai first.
"""
import argparse, math, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = ["references/knowledge", "references/checklists"]
STOP = set("a an the and or of to in on for with is are be by as at it this that from your you how what why when which do does can into vs not".split())
SYN = {  # light query expansion so short queries still hit
    "aeo": ["answer", "engine"], "geo": ["generative", "engine"], "llm": ["model", "chatgpt"],
    "citation": ["cite", "cited", "source"], "schema": ["structured", "jsonld", "markup"],
    "backlink": ["link", "links"], "review": ["reviews", "ratings"], "keyword": ["topic", "query", "prompt"],
    "brand": ["entity", "branding"], "speed": ["performance", "vitals"], "crawl": ["crawler", "robots", "index"],
}


def tok(s):
    words = re.findall(r"[a-z0-9]+", s.lower().replace("-", " "))
    out = []
    for w in words:
        if w in STOP or len(w) < 2:
            continue
        out.append(w[:-1] if len(w) > 4 and w.endswith("s") else w)
    return out


def load():
    chunks = []
    for d in DIRS:
        for f in sorted((ROOT / d).glob("*.md")):
            text = f.read_text(encoding="utf-8")
            meta = {}
            m = re.match(r"---\n(.*?)\n---\n", text, re.S)
            if m:
                for line in m.group(1).splitlines():
                    if ":" in line:
                        k, v = line.split(":", 1)
                        meta[k.strip()] = v.strip()
                text = text[m.end():]
            parts = re.split(r"(?m)^## ", text)
            head = meta.get("title", f.stem)
            for i, p in enumerate(parts):
                if not p.strip():
                    continue
                heading = "(intro)" if i == 0 else p.splitlines()[0].strip()
                body = p if i == 0 else "## " + p
                chunks.append({"file": f"{d}/{f.name}", "title": head, "heading": heading,
                               "tags": meta.get("tags", ""), "text": body.strip()})
    return chunks


def bm25(chunks, query, k1=1.4, b=0.75):
    q = tok(query)
    q += [s for w in q for s in SYN.get(w, [])]
    docs = [tok(c["text"]) for c in chunks]
    N = len(docs)
    avg = sum(map(len, docs)) / max(N, 1)
    df = {}
    for d in docs:
        for w in set(d):
            df[w] = df.get(w, 0) + 1
    scores = []
    for c, d in zip(chunks, docs):
        tf = {}
        for w in d:
            tf[w] = tf.get(w, 0) + 1
        s = 0.0
        for w in set(q):
            if w not in tf:
                continue
            idf = math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5))
            s += idf * tf[w] * (k1 + 1) / (tf[w] + k1 * (1 - b + b * len(d) / avg))
        meta = set(tok(c["heading"] + " " + c["title"] + " " + c["tags"]))
        s += 1.2 * len(meta & set(q))
        scores.append(s)
    return sorted(zip(scores, chunks), key=lambda x: -x[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("-k", type=int, default=6)
    ap.add_argument("--list", action="store_true", help="show headings only")
    ap.add_argument("--section", help="print every chunk whose heading contains this text")
    a = ap.parse_args()
    chunks = load()
    if a.section:
        for c in chunks:
            if a.section.lower() in c["heading"].lower():
                print(f"\n### {c['file']} — {c['title']}\n{c['text']}\n")
        return
    if not a.query:
        ap.print_help(); sys.exit(1)
    hits = [h for h in bm25(chunks, a.query) if h[0] > 0][: a.k]
    if not hits:
        print("No match. Try other English keywords or `--list`."); return
    for s, c in hits:
        if a.list:
            print(f"{s:6.2f}  {c['file']}  ›  {c['heading']}")
        else:
            print(f"\n=== {c['file']} › {c['heading']}  (score {s:.2f}) ===\n{c['text']}\n")


if __name__ == "__main__":
    main()
