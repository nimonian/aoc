from pathlib import Path

path = Path(__file__).parent / "input.txt"
grid = path.read_text().strip().splitlines()


def solution():
    result = 0
    rows, cols = len(grid), len(grid[0])
    targets = ["SM", "MS"]

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                d1 = grid[r - 1][c - 1] + grid[r + 1][c + 1]
                d2 = grid[r - 1][c + 1] + grid[r + 1][c - 1]

                result += d1 in targets and d2 in targets

    return result
