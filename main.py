"""Track new-hire onboarding completion from a checklist CSV.

Usage: python3 main.py checklist.csv
CSV columns: employee,task,done (yes/no).
Completion percent per employee, lowest first, so stragglers are
visible; employees with no tasks are reported at 0%.
"""
import argparse, csv, sys
from collections import Counter


def progress(rows):
    totals, done = Counter(), Counter()
    for row in rows:
        employee = row["employee"].strip()
        totals[employee] += 1
        if row["done"].strip().lower() == "yes":
            done[employee] += 1
    out = [(e, (done[e] / totals[e]) if totals[e] else 0.0, totals[e])
           for e in totals]
    return sorted(out, key=lambda r: r[1])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for employee, pct, total in progress(list(csv.DictReader(f))):
            print(f"{employee}: {pct:.0%} complete ({total} tasks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
