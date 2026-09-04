#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
DATE_NAME = re.compile(r"^\d{4}-\d{2}-\d{2}\.md$")
WEEK_NAME = re.compile(r"^\d{4}-W\d{2}\.md$")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("# "):
        errors.append("缺少一级标题")
    if len(text.strip()) < 500:
        errors.append("正文少于 500 字符，疑似不完整")
    if "http://" not in text and "https://" not in text:
        errors.append("未发现来源链接")
    if path.parent.name == "daily" and not DATE_NAME.match(path.name):
        errors.append("日报文件名应为 YYYY-MM-DD.md")
    if path.parent.name == "weekly" and not WEEK_NAME.match(path.name):
        errors.append("周报文件名应为 YYYY-Www.md")
    return errors


def main() -> None:
    paths = [Path(arg).resolve() for arg in sys.argv[1:]]
    if not paths:
        paths = sorted(REPORTS.glob("*/*.md"))
    failed = False
    for path in paths:
        if REPORTS not in path.parents or not path.exists():
            print(f"ERROR {path}: 不是有效的报告文件")
            failed = True
            continue
        errors = validate(path)
        if errors:
            print(f"ERROR {path.relative_to(ROOT)}: {'；'.join(errors)}")
            failed = True
        else:
            print(f"OK {path.relative_to(ROOT)}")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()

