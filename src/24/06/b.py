from pathlib import Path

path = Path(__file__).parent / "input.txt"


def get_origin(M):
    for r in range(len(M)):
        for c in range(len(M[0])):
            if M[r][c] == "^":
                return r, c


rotate = lambda x, y: (y, -x)

in_map = lambda M, x, y: x in range(len(M)) and y in range(len(M[0]))


def get_map(M, r, c):
    _M = [list(row) for row in M]
    _M[r][c] = "#"
    return _M


def gen_path(M, r, c):
    dr, dc = -1, 0
    yield r, c, dr, dc

    while in_map(M, r + dr, c + dc):
        if M[r + dr][c + dc] == "#":
            dr, dc = rotate(dr, dc)
            continue

        r, c = r + dr, c + dc
        yield r, c, dr, dc


def contains_loop(M, r, c):
    visited = {}

    for r, c, dr, dc in gen_path(M, r, c):
        if (dr, dc) in visited.get((r, c), []):
            return True

        visited[(r, c)] = visited.get((r, c), []) + [(dr, dc)]

    return False


def solution():
    M = path.read_text().strip().splitlines()
    r0, c0 = get_origin(M)
    i, count, n = 0, 0, len(M) * len(M[0])

    for x in range(len(M)):
        for y in range(len(M[0])):
            i += 1
            print(f"{i} / {n}")
            if M[x][y] == "#":
                continue

            count += contains_loop(get_map(M, x, y), r0, c0)

    return count
