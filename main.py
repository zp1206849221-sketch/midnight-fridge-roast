"""Midnight Fridge Roast — one-line entry for make.fun.

Writes a single roast line to /output/entry.txt.
The target: a smart fridge that refuses to open after midnight.
"""

import os

LINE = (
    "My smart fridge locks at midnight like I'm not on the list: me, barefoot "
    "in my own kitchen, denied VIP access to leftover lasagna and a drawer "
    "of dead lettuce."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
