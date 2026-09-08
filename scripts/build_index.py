#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "INDEX.md"
START = "<!-- AUTO-GENERATED:START -->"
END = "<!-- AUTO-GENERATED:END -->"


def title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def section(label: str, directory: Path) -> str:
    files = sorted((path for path in directory.glob("*.md") if path.name != "README.md"), reverse=True) if directory.exists() else []
    # Product reports are often drafted alongside a radar run.  Only index files
    # already in Git so a daily publication cannot expose an unrelated draft.
    if directory.name == "products":
        tracked = set(
            subprocess.run(
                ["git", "ls-files", "-z", "--", str(directory.relative_to(ROOT))],
                cwd=ROOT,
                check=True,
                capture_output=True,
                text=True,
            ).stdout.split("\0")
        )
        files = [path for path in files if path.relative_to(ROOT).as_posix() in tracked]
    lines = [f"## {label}", ""]
    if not files:
        return "\n".join(lines + ["暂无报告。", ""])
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        lines.append(f"- [{title(path)}](./{rel})")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    current = INDEX.read_text(encoding="utf-8")
    generated = "\n".join(
        [
            "本页由 `scripts/build_index.py` 自动生成。",
            "",
            section("日报", ROOT / "reports" / "daily"),
            section("周报", ROOT / "reports" / "weekly"),
            section("产品发布深度调研", ROOT / "reports" / "products"),
        ]
    ).rstrip()
    replacement = f"{START}\n\n{generated}\n\n{END}"
    updated, count = re.subn(
        re.escape(START) + r".*?" + re.escape(END),
        replacement,
        current,
        flags=re.DOTALL,
    )
    if count != 1:
        raise SystemExit("INDEX.md 缺少唯一的自动生成标记")
    INDEX.write_text(updated.rstrip() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
