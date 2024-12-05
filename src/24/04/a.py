from pathlib import Path

path = Path(__file__).parent / "input.txt"
grid = path.read_text().strip().splitlines()


def solution():
    result = 0
    rows, cols = len(grid), len(grid[0])
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in dirs:
                word = "".join(
                    grid[r + k * dr][c + k * dc]
                    for k in range(4)
                    if r + k * dr in range(rows) and c + k * dc in range(cols)
                )

                result += word == "XMAS"

    return result
