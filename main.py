"""Write a one-line office joke to /output/entry.txt.

The joke is about a recurring meeting that outgrew its name:
it started as a quick sync and ended up with a calendar invite
of its own and, finally, a performance review.
"""

import os

JOKE = "Our 'quick sync' has its own recurring calendar invite and, as of today, a performance review."


def main() -> None:
    output_path = "/output/entry.txt"
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
