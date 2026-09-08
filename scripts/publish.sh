#!/usr/bin/env bash
set -euo pipefail

repo_root="$(git rev-parse --show-toplevel)"
cd "$repo_root"

python3 scripts/validate_reports.py
python3 scripts/validate_events.py
python3 scripts/build_index.py

publish_target="${1:-report update}"
report_type="${publish_target%% *}"
report_period="${publish_target#* }"

case "$report_type" in
  daily)
    staged_paths=("reports/daily/${report_period}.md" "data/events/${report_period}.json")
    ;;
  weekly)
    staged_paths=("reports/weekly/${report_period}.md")
    ;;
  *)
    echo "Unsupported publication target: $publish_target" >&2
    exit 2
    ;;
esac

# A scheduled report must never stage unrelated user drafts from broad folders.
git add -- INDEX.md data/source-state.json "${staged_paths[@]}"

if git diff --cached --quiet; then
  echo "没有需要发布的变化。"
  exit 0
fi

message="radar: publish ${publish_target}"
git commit -m "$message"

if git remote get-url origin >/dev/null 2>&1; then
  git pull --rebase origin main
  git push origin main
else
  echo "尚未配置 origin；已完成本地提交。" >&2
  exit 2
fi
