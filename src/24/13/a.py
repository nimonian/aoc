from pathlib import Path
import re


def cost(game):
    u1, u2, v1, v2, w1, w2 = map(int, re.findall(r"(\d+)", game))
    a = (v2 * w1 - v1 * w2) / (u1 * v2 - v1 * u2)
    b = (u1 * w2 - u2 * w1) / (u1 * v2 - v1 * u2)
    return 3 * a + b if a == int(a) and b == int(b) else 0


def solution():
    path = Path(__file__).parent / "input.txt"
    return sum(map(cost, path.read_text().strip().split("\n\n")))
