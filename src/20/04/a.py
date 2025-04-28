from pathlib import Path
import re


txt = Path(__file__).parent / "test_input.txt"


def parse(raw):
    return {
        "byr": re.match("byr:(\w+)", raw),
        "iyr": re.match("iyr:(\w+)", raw),
        "eyr": re.match("eyr:(\w+)", raw),
        "hgt": re.match("hgt:(\w+)", raw),
        "hcl": re.match("hgt:(\w+)", raw),
        "ecl": re.match("ecl:(\w+)", raw),
        "pid": re.match("pid:(\w+)", raw),
    }


def solution():
    passports = txt.read_text().split("\n\n")
    parsed = [parse(p) for p in passports]
    print(parsed)
    return sum(all(p.values()) for p in parsed)
