from pathlib import Path

path = Path(__file__).parent / "input.txt"
parts = path.read_text().strip().split("\n\n")


def solution():
    order = {}
    good = []

    for line in parts[0].splitlines():
        a, b = line.split("|")
        order[a] = order.get(a, []) + [b]

    for line in parts[1].splitlines():
        X = line.split(",")
        if all(b in order.get(a, []) for a, b in zip(X[:-1], X[1:])):
            good.append(X)

    return sum(int(X[(len(X) - 1) // 2]) for X in good)
