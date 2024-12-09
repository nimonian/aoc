from pathlib import Path
from functools import reduce

path = Path(__file__).parent / "input.txt"
nums = [int(x) for x in path.read_text().strip()]


def get_system():
    files, space = [], []
    addr = 0

    for i in range(len(nums) // 2):
        files.append({"addr": addr, "size": nums[2 * i], "val": i})
        addr += files[-1]["size"]

        space.append({"addr": addr, "size": nums[2 * i + 1]})
        addr += space[-1]["size"]

    files.append({"addr": addr, "size": nums[-1], "val": len(nums) // 2})

    return files, space


def calculate_checksum(files):
    checksum = 0

    for f in files:
        a, n, v = f["addr"], f["size"], f["val"]
        checksum += (n * a + (n * n - n) // 2) * v

    return checksum


def solution():
    files, space = get_system()

    for f in files[::-1]:
        check = [s for s in space if s["addr"] < f["addr"]]

        for s in sorted(check, key=lambda s: s.get("addr")):
            if f["size"] <= s["size"]:
                # release old space
                space.append({"addr": f["addr"], "size": f["size"]})

                # reserve new space
                s["size"] -= f["size"]

                # move the file
                f["addr"] = s["addr"]

                # relocate remaining space
                s["addr"] += f["size"]

                break

    return calculate_checksum(files)
