import os

WEEK_LINE = "1,200 words written, 40 kept, $0 paid — I mined a mountain and pocketed gravel."


def emit() -> None:
    if not WEEK_LINE.strip():
        raise ValueError("week line must not be blank")
    if len(WEEK_LINE) > 100:
        raise ValueError("week line exceeds 100 characters")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target_dir, exist_ok=True)
    destination = os.path.join(target_dir, "entry.txt")
    with open(destination, "wb") as handle:
        handle.write(WEEK_LINE.encode("utf-8"))


if __name__ == "__main__":
    emit()
