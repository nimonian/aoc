from pathlib import Path


def solution():
    file = Path(__file__).parent / "input.txt"
    lines = file.read_text().splitlines()
    m, n = len(lines[0]), len(lines)

    counts = [0 for _ in range(m)]

    for line in lines:
        for i, char in enumerate(line):
            counts[i] += char == "1"

    digits = ["1" if (count > n / 2) else "0" for count in counts]

    binary = "".join(digits)

    a = int(binary, 2)
    b = a ^ (2**m - 1)

    return a * b
