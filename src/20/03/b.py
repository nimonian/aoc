from pathlib import Path
from src.utils import prod

txt = Path(__file__).parent / "input.txt"
grid = txt.read_text().splitlines()


def count_trees(dr, dc):
    count = 0
    r, c = 0, 0
    cols = len(grid[0])

    while r + dr < len(grid):
        r, c = r + dr, (c + dc) % cols
        count += grid[r][c] == "#"

    return count


def solution():
    cases = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    return prod(count_trees(*case) for case in cases)
