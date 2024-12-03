from pathlib import Path
from pydantic import List
from src.utils import compose


def parse_grid(txt: str) -> List[List[int]]:
    lines = txt.splitlines()


def solution():
    path = Path(__file__).parent / "input.txt"
    parts = path.read_text().split("\n\n")

    nums = map(int, parts[0].split(","))
    grids = map(parse_grid, parts[1:])
