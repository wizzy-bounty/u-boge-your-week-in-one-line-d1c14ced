import os

LINE = "9 dinners cooked, 1 edible, $3.17 on takeout — my stove now accepts bribes."


def main() -> None:
    if not LINE.strip():
        raise ValueError("entry must not be blank")
    if len(LINE) > 100:
        raise ValueError("entry exceeds 100 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
