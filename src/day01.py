DAY = 1


def part1(inp: list[str]) -> int:
    l1 = []
    l2 = []

    for line in inp:
        x1, x2 = [int(x) for x in line.split()]

        l1.append(x1)
        l2.append(x2)

    l1.sort()
    l2.sort()

    s = 0
    for x1, x2 in zip(l1, l2):
        s += abs(x1 - x2)

    return s


def part2(inp: list[str]) -> int:
    m1 = {}
    m2 = {}

    for line in inp:
        x1, x2 = [int(x) for x in line.split()]

        m1[x1] = m1.get(x1, 0) + 1
        m2[x2] = m2.get(x2, 0) + 1

    s = 0
    for k, v1 in m1.items():
        if k in m2:
            s += k * m2[k] * v1

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
