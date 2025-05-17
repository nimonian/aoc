from pathlib import Path


txt = Path(__file__).parent / "input.txt"


def count(group):
    s = set(group.replace("\n", ""))
    return len(s)


def solution():
    groups = txt.read_text().split("\n\n")
    return sum(map(count, groups))
