from pathlib import Path


txt = Path(__file__).parent / "input.txt"


def count(group):
    sets = map(set, group.split("\n"))
    return len(set.intersection(*sets))


def solution():
    groups = txt.read_text().split("\n\n")
    return sum(map(count, groups))
