from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
# Specific, non-round total from accumulated browsing sessions.
TAB_COUNT = "173"


def write_entry() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TAB_COUNT, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
