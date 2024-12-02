DAY = 2


def is_safe(levels: list[int]) -> bool:
    increasing = True if levels[0] < levels[1] else False

    for i in range(len(levels) - 1):
        if increasing and levels[i] >= levels[i + 1]:
            return False

        if not increasing and levels[i] <= levels[i + 1]:
            return False

        diff = abs(levels[i] - levels[i + 1])
        if diff > 3:
            return False

    return True


def part1(inp: list[str]) -> int:
    safe = 0

    for line in inp:
        levels = [int(x) for x in line.split()]

        if is_safe(levels):
            safe += 1

    return safe


def part2(inp: list[str]) -> int:
    safe = 0

    for line in inp:
        levels = [int(x) for x in line.split()]
        if is_safe(levels):
            safe += 1
            continue

        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1 :]):
                safe += 1
                break

    return safe


def read_input_file(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf8") as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == "__main__":
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
