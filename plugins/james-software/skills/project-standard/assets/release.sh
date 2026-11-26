#!/usr/bin/env bash
# Promote main to production. This is the only way production changes.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
[[ "$(git branch --show-current)" == main ]] || { echo "release from main" >&2; exit 1; }
[[ -z "$(git status --porcelain --untracked-files=no)" ]] || { echo "commit first" >&2; exit 1; }
git fetch -q origin
if git rev-parse -q --verify refs/remotes/origin/main >/dev/null; then
  git merge-base --is-ancestor origin/main HEAD || { echo "pull main first" >&2; exit 1; }
fi
git push -q origin main

index="$(mktemp -u)"
trap 'rm -f "$index"' EXIT
GIT_INDEX_FILE="$index" git read-tree HEAD
if [[ -f .release-exclude ]]; then excludes="$(grep -Ev '^[[:space:]]*(#|$)' .release-exclude || true)"; else excludes=$'ai-context\ntests'; fi
while IFS= read -r path; do
  [[ -n "$path" ]] && GIT_INDEX_FILE="$index" git rm -rqf --cached --ignore-unmatch -- "$path"
done <<<"$excludes"
tree="$(GIT_INDEX_FILE="$index" git write-tree)"
parent="$(git rev-parse -q --verify refs/remotes/origin/production || true)"
if [[ -n "$parent" && "$(git rev-parse "$parent^{tree}")" == "$tree" ]]; then
  echo "production already current"
  exit 0
fi
commit="$(git commit-tree "$tree" ${parent:+-p "$parent"} -m "production: $(git log -1 --format='%h %s')")"
git push origin "$commit:refs/heads/production"
