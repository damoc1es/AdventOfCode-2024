from functools import cmp_to_key

DAY = 5


def parse_input(inp: list[str]) -> tuple[list[list[int]], dict[int, list[int]]]:
    priorities = []
    updates = []

    print_stage = False
    for line in inp:
        if line == "":
            print_stage = True
            continue

        if print_stage:
            updates.append(list(int(x) for x in line.split(",")))
        else:
            priorities.append(tuple(int(x) for x in line.split("|")))

    after = {}
    for a, b in priorities:
        if a in after.keys():
            after[a].append(b)
        else:
            after[a] = [b]

    return updates, after


def part1(inp: list[str]) -> int:
    updates, after = parse_input(inp)

    s = 0
    for book in updates:
        bad = False
        for i in range(len(book)):
            for j in range(i + 1, len(book)):
                if book[j] in after.keys() and book[i] in after[book[j]]:
                    bad = True
                    break
            if bad:
                break

        if not bad:
            s += book[len(book) // 2]

    return s


def part2(inp: list[str]) -> int:
    updates, after = parse_input(inp)

    def cmp(a: int, b: int) -> int:
        if a in after.keys() and b in after[a]:
            return -1
        if b in after.keys() and a in after[b]:
            return 1
        return 0

    s = 0
    for book in updates:
        new = sorted(book, key=cmp_to_key(cmp))

        if book != new:
            s += new[len(new) // 2]

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
