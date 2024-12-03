import re

DAY = 3


def part1(inp: list[str]) -> int:
    s = 0
    for line in inp:
        matches = re.findall(r"mul\(\d+,\d+\)", line)
        for m in matches:
            a, b = m.split(",")
            a = int(a[4:])
            b = int(b[:-1])

            s += a * b

    return s


def part2(inp: list[str]) -> int:
    s = 0
    on = True
    for line in inp:
        matches = re.findall(r"(mul\(\d+,\d+\))|(don't\(\))|(do\(\))", line)

        for m in matches:
            if m[1] == "don't()":
                on = False
            elif m[2] == "do()":
                on = True
            elif m[0] != "" and on:
                a, b = m[0].split(",")
                a = int(a[4:])
                b = int(b[:-1])

                s += a * b

    return s


def read_input_file(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf8") as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == "__main__":
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
