from pathlib import Path
from functools import cmp_to_key

path = Path(__file__).parent / "input.txt"
parts = path.read_text().strip().split("\n\n")


def solution():
    order = {}
    bad = []

    for line in parts[0].splitlines():
        a, b = line.split("|")
        order[a] = order.get(a, []) + [b]

    for line in parts[1].splitlines():
        X = line.split(",")
        if not all(b in order.get(a, []) for a, b in zip(X[:-1], X[1:])):
            bad.append(X)

    cmp = lambda a, b: -1 if b in order.get(a, []) else 1

    for X in bad:
        print(X)
        X.sort(key=cmp_to_key(cmp))
        print(X, "\n")

    return sum(int(X[(len(X) - 1) // 2]) for X in bad)
