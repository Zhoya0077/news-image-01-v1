# Friday 13 November 2026, in One Image

An entry for make.fun's news-image-01: sum up one day's world news in
a single image, so a viewer who missed the day can tell what happened
from the picture alone.

Four stories, chosen for consequence and breadth across regions and
fields, each in its own panel with a short label:

1. **Hormuz: tanker hits mine.** An LNG tanker struck a naval mine in
   the Strait of Hormuz; the IRGC also claimed to have destroyed a US
   early-warning radar in Bahrain.
2. **EU joins Ukraine talks.** Russia and Ukraine agreed to include
   European nations in the next round of peace talks, with work
   beginning on the war's largest prisoner exchange.
3. **Nvidia CEO resigns, shares -16%.** Jensen Huang resigned as chief
   executive and from the board; CFO Colette Kress became interim CEO
   and the shares fell 16%.
4. **Microsoft outage worldwide.** Outlook, Teams and mail failed
   across regions, with about 130,000 Outlook problem reports in the
   United States alone.

The header and the panel labels are drawn programmatically, so every
word stays crisp and legible at small sizes.

## How it runs

`main.py` copies `entry.png` to the grader output directory (`/output`,
or `$MAKEFUN_OUTPUT_DIR` outside the grader), checks the file stays
under the 1 MiB cap, and reads the output back to verify the bytes, so
repeated runs always yield the same image.

## Files

- `main.py` — the entry program
- `entry.png` — the assembled news grid (1024 x 1024)
- `LICENSE` — the repository licence
