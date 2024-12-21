from pathlib import Path


def transform(L):
    result = []

    for x in L:
        y = str(x)
        if x == 0:
            result.append(1)

        elif len(y) % 2 == 0:
            result.append(int(y[: len(y) // 2]))
            result.append(int(y[len(y) // 2 :]))

        else:
            result.append(x * 2024)

    return result


def solution():
    path = Path(__file__).parent / "input.txt"
    nums = [int(n) for n in path.read_text().strip().split(" ")]

    for i in range(25):
        nums = transform(nums)

    return len(nums)
