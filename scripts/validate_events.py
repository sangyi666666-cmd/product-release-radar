#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import json
import sys
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / "data" / "events"
REQUIRED = {
    "id",
    "published_at",
    "collected_at",
    "lane",
    "source_tier",
    "entity",
    "signal_type",
    "title",
    "facts",
    "source_urls",
    "analysis",
    "insight",
    "recommended_action",
    "confidence",
    "score",
}


def valid_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"JSON 无法读取：{exc}"]
    if not isinstance(payload, list):
        return ["顶层必须是数组"]
    for index, event in enumerate(payload):
        prefix = f"第 {index + 1} 条"
        if not isinstance(event, dict):
            errors.append(f"{prefix}不是对象")
            continue
        missing = sorted(REQUIRED - event.keys())
        if missing:
            errors.append(f"{prefix}缺少字段：{', '.join(missing)}")
        if event.get("source_tier") not in {"P0", "P1", "P2", "internal"}:
            errors.append(f"{prefix} source_tier 无效")
        if event.get("confidence") not in {"high", "medium", "low"}:
            errors.append(f"{prefix} confidence 无效")
        score = event.get("score")
        if not isinstance(score, int) or not 0 <= score <= 100:
            errors.append(f"{prefix} score 应为 0～100 的整数")
        facts = event.get("facts")
        if not isinstance(facts, list) or not facts or not all(isinstance(v, str) and v.strip() for v in facts):
            errors.append(f"{prefix} facts 应为非空字符串数组")
        urls = event.get("source_urls")
        if not isinstance(urls, list) or not urls or not all(valid_url(v) for v in urls):
            errors.append(f"{prefix} source_urls 应为非空 HTTP(S) 链接数组")
    return errors


def main() -> None:
    paths = sorted(EVENTS.glob("*.json"))
    failed = False
    for path in paths:
        errors = validate(path)
        if errors:
            print(f"ERROR {path.relative_to(ROOT)}: {'；'.join(errors)}")
            failed = True
        else:
            print(f"OK {path.relative_to(ROOT)}")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()

