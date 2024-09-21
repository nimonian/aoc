from pathlib import Path


def col_char_count(A, i, char):
    col = [row[i] for row in A]
    return sum(x == char for x in col)


def a(lines):
    A = [a for a in lines]
    i = 0

    while len(A) > 1:
        count = col_char_count(A, i, "1")
        char = "1" if count >= len(A) / 2 else "0"
        A = [a for a in A if a[i] == char]
        i += 1

    return int("".join(A[0]), 2)


def b(lines):
    B = [b for b in lines]
    j = 0

    while len(B) > 1:
        count = col_char_count(B, j, "1")
        char = "1" if count < len(B) / 2 else "0"
        B = [b for b in B if b[j] == char]
        j += 1

    return int("".join(B[0]), 2)


def solution():
    file = Path(__file__).parent / "input.txt"
    lines = file.read_text().splitlines()

    return a(lines) * b(lines)
