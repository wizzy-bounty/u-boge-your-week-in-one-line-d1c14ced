from pathlib import Path
import os

LINE = "Hit inbox zero on Monday; 312 emails later, my inbox is a tide that only comes in."


def emit() -> None:
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    target_dir.mkdir(parents=True, exist_ok=True)
    if not 1 <= len(LINE) <= 100:
        raise ValueError("entry line outside the 1-100 character gate")
    (target_dir / "entry.txt").write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    emit()
