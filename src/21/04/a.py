from pathlib import Path


def get_col(grid, i):
    return [row[i] for row in grid]


def calculate_score(grid):
    print(grid)
    total = 0
    for row in grid:
        for n in row:
            if n != True:
                total += int(n)

    return total


def get_row(row):
    split_row = row.split(" ")

    return [n for n in split_row if n.isdigit()]


def solution():

    file = Path(__file__).parent / "input.txt"
    parts = file.read_text().split("\n\n")

    nums = parts.pop(0).split(",")

    grids = []

    for part in parts:
        grids.append([get_row(row) for row in part.split("\n")])

    for num in nums:
        for grid in grids:
            for row in grid:
                for i, n in enumerate(row):
                    if n == num:
                        row[i] == Trueif is_winning(grid):
                            return num * calculate_score(grid)

                        if all(n == True for n in row):
                            return calculate_score(grid)

                        if all(n == True for n in get_col(grid, i)):
                            return calculate_score(grid)
