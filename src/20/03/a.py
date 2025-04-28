from pathlib import Path

txt = Path(__file__).parent / "input.txt"
grid = txt.read_text().splitlines()


def solution():
    count = 0
    r, c = 0, 0
    dr, dc = 1, 3
    cols = len(grid[0])

    while r + dr < len(grid):
        r, c = r + dr, (c + dc) % cols
        count += grid[r][c] == "#"

    return count
