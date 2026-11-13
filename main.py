# news-image-01 entry v1: copies the assembled news grid to /output/entry.png.
# Python 3.13, standard library only, deterministic, no network.
# The image sums up Friday 13 November 2026 in four panels: a tanker
# striking a mine in the Strait of Hormuz, Europe joining the Ukraine
# peace talks, the Nvidia chief executive resigning as shares fall 16%,
# and a worldwide Microsoft outage. The header and panel labels are
# drawn programmatically so every word stays crisp at any size.
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
MAX_BYTES = 1_048_576


def main():
    data = SOURCE.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.png exceeds the 1 MiB cap")
    out = Path(OUTPUT_DIR) / "entry.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out)
    if out.read_bytes() != data:
        raise SystemExit("output bytes differ from entry.png")


if __name__ == "__main__":
    main()
