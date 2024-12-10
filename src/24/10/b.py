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
        return 1

    steps = get_valid_steps(r, c)

    if len(steps) == 0:
        0

    return sum(find_paths(r, c) for r, c in steps)


def solution():
    result = 0

    for r in range(len(M)):
        for c in range(len(M[0])):
            if M[r][c] == 0:
                result += find_paths(r, c)

    return result
