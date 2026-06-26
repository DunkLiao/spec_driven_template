#!/usr/bin/env python3
"""Scaffold the Spec-Driven Development (SDD) template files into a project folder.

Copies the blank SDD templates (constitution / spec / design / tasks / CLAUDE.md /
prompts / README) from the skill's bundled templates into a destination folder so
the user can start a new feature or project. The worked example is copied only when
--with-example is passed.

Usage:
  python scaffold.py                      # -> output/sdd-template/
  python scaffold.py --dest output/my-app # custom destination
  python scaffold.py --with-example       # also include the borrower-lookup example
"""
import argparse
import shutil
from pathlib import Path

CORE_FILES = [
    "README.md",
    "CLAUDE.md",
    "prompts.md",
    "00-constitution.md",
    "01-spec.md",
    "02-design.md",
    "03-tasks.md",
]
EXAMPLE_DIR = "範例-borrower-lookup"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dest", default="output/sdd-template",
                    help="Destination folder (default: output/sdd-template)")
    ap.add_argument("--with-example", action="store_true",
                    help="Also copy the worked example folder")
    args = ap.parse_args()

    src = Path(__file__).resolve().parent.parent / "references" / "templates"
    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    copied = []
    for name in CORE_FILES:
        s = src / name
        if s.exists():
            shutil.copy2(s, dest / name)
            copied.append(name)

    if args.with_example:
        ex_src = src / EXAMPLE_DIR
        ex_dest = dest / EXAMPLE_DIR
        if ex_src.exists():
            shutil.copytree(ex_src, ex_dest, dirs_exist_ok=True)
            copied.append(EXAMPLE_DIR + "/ (worked example)")

    print(f"Scaffolded SDD templates into: {dest}")
    for c in copied:
        print(f"  - {c}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
