from pathlib import Path
import re


txt = Path(__file__).parent / "input.txt"


def check_byr(raw):
    match = re.search("byr:(\d+)", raw)

    if match is None:
        return False

    byr = match.group(1)
    return 1920 <= int(byr) <= 2002


def check_iyr(raw):
    match = re.search("iyr:(\d+)", raw)

    if match is None:
        return False

    iyr = match.group(1)
    return 2010 <= int(iyr) <= 2020


def check_eyr(raw):
    match = re.search("eyr:(\d+)", raw)

    if match is None:
        return False

    eyr = match.group(1)
    return 2020 <= int(eyr) <= 2030


def check_hgt(raw):
    match = re.search("hgt:(\d+)(cm|in)", raw)

    if match is None:
        return False

    h, unit = match.group(1), match.group(2)

    if unit == "cm":
        return 150 <= int(h) <= 193

    if unit == "in":
        return 59 <= int(h) <= 76

    return False


def check_hcl(raw: str) -> bool:
    match = re.search("hcl:(#[0-9|a-f]{6})", raw)
    return bool(match)


def check_ecl(raw: str) -> bool:
    match = re.search("ecl:([a-z]+)", raw)

    if match is None:
        return False

    ecl = match.group(1)
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(raw: str) -> bool:
    match = re.search("[0-9]{9}", raw)
    return bool(match)


validations = [
    check_byr,
    check_iyr,
    check_eyr,
    check_hgt,
    check_hcl,
    check_ecl,
    check_pid,
]


def valid(raw: str) -> bool:
    return all(v(raw) for v in validations)


def solution():
    raws = txt.read_text().split("\n\n")
    return sum(valid(raw) for raw in raws)
