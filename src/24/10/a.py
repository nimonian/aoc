from pathlib import Path
from functools import lru_cache, reduce

path = Path(__file__).parent / "input.txt"
lines = path.read_text().strip().splitlines()
M = [list(map(int, list(line))) for line in lines]


def get_valid_steps(r, c):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    return [
        (r + dr, c + dc)
        for dr, dc in dirs
        if r + dr in range(len(M))
        and c + dc in range(len(M[0]))
        and M[r + dr][c + dc] == M[r][c] + 1
    ]


@lru_cache
def find_paths(r, c):
    if M[r][c] == 9:
        return set([(r, c)])

    steps = get_valid_steps(r, c)

    if len(steps) == 0:
        return set()

    return reduce(lambda x, y: x.union(y), [find_paths(r, c) for r, c in steps], set())


def solution():
    result = {}

    for r in range(len(M)):
        for c in range(len(M[0])):
            if M[r][c] == 0:
                result[(r, c)] = find_paths(r, c)

    return sum(len(p) for p in result.values())
