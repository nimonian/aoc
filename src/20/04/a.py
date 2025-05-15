from pathlib import Path


txt = Path(__file__).parent / "input.txt"
P = txt.read_text().split("\n\n")
R = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def solution():
    return sum(all(r in p for r in R) for p in P)
