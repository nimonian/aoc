from pathlib import Path


def solution():
    file = Path(__file__).parent / "input.txt"
    lines = file.read_text().splitlines()
    movements = {"forward": (1, 0), "up": (0, -1), "down": (0, 1)}
    x, y, z = (0, 0, 0)

    for line in lines:
        direction, magnitude = line.strip().split(" ")
        magnitude = int(magnitude)
        dx, dy = movements[direction]

        x += magnitude * dx
        z += magnitude * dy
        y += dx and z * magnitude

    return x * y
