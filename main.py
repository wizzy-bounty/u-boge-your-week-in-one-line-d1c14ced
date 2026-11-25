import os
from pathlib import Path

ENTRY = "This week I lost my keys 9 times; the couch cushions now charge rent."


def main() -> None:
    if not ENTRY.strip() or len(ENTRY) > 100:
        raise ValueError("entry must contain 1 to 100 characters")
    output_dir = Path(os.getenv("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
