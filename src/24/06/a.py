from pathlib import Path

path = Path(__file__).parent / "input.txt"
M = path.read_text().strip().splitlines()
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_origin():
    for r in range(len(M)):
        for c in range(len(M[r])):
            if M[r][c] == "^":
                return r, c


def on_edge(r, c):
    return r in [0, len(M) - 1] or c in [0, len(M[0]) - 1]


def solution():
    r, c = get_origin()
    i = 0
    dr, dc = dirs[i]
    visited = {(r, c): True}

    while not on_edge(r, c):

        if M[r + dr][c + dc] == '#':
            i = (i + 1) % 4
            dr, dc = dirs[i]
        
        r, c = r + dr, c + dc
        visited[(r, c)] = True

    return len(visited)
