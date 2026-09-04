#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

python3 scripts/validate_reports.py
python3 scripts/build_index.py

git add README.md INDEX.md config data research reports scripts templates .github

if git diff --cached --quiet; then
  echo "没有需要发布的变化。"
  exit 0
fi

message="radar: publish ${1:-report update}"
git commit -m "$message"

if git remote get-url origin >/dev/null 2>&1; then
  git pull --rebase origin main
  git push origin main
else
  echo "尚未配置 origin；已完成本地提交。" >&2
  exit 2
fi

