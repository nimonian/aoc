from pathlib import Path

path = Path(__file__).parent / "input.txt"
M0 = path.read_text().strip().splitlines()
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_origin():
    for r in range(len(M0)):
        for c in range(len(M0[r])):
            if M0[r][c] == "^":
                return r, c


def on_edge(r, c):
    return r in [0, len(M0) - 1] or c in [0, len(M0[0]) - 1]


def has_loop(r0, c0, M):
    r, c = r0, c0
    i = 0
    dr, dc = dirs[i]
    visited = {(r, c): [(dr, dc)]}

    while not on_edge(r, c):
        if M[r + dr][c + dc] == "#":
            i = (i + 1) % 4
            dr, dc = dirs[i]

        r, c = r + dr, c + dc

        if (dr, dc) in visited.get((r, c), []):
            return True

        visited[(r, c)] = visited.get((r, c), []) + [(dr, dc)]

    return False


def solution():
    result = 0
    count = 0
    r0, c0 = get_origin()

    for r in range(len(M0)):
        for c in range(len(M0[0])):
            count += 1
            print(f"{count / 130 ** 2 * 100}%")

            if M0[r][c] == "#":
                continue

            M = [list(row) for row in M0]
            M[r][c] = "#"

            result += has_loop(r0, c0, M)

    return result
