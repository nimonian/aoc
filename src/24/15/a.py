from pathlib import Path
import re

dirs = {">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0)}


def parse_input(txt: str):
    parts = txt.split("\n\n")
    grid = [list(line) for line in parts[0].splitlines()]
    symbols = re.findall(r"[>^<v]", parts[1])

    return grid, symbols


def find_origin(grid):
    for r, row in enumerate(grid):
        for c, char in enumerate(row):
            if char == "@":
                return r, c


def solution():
    path = Path(__file__).parent / "input.txt"
    grid, symbols = parse_input(path.read_text())
    r0, c0 = find_origin(grid)

    for sym in symbols:
        dr, dc = dirs.get(sym)
        blob = [(r0, c0)]
