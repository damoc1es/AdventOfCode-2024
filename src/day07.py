from typing import Callable

DAY = 7


def solve(
    desired: int,
    lst: tuple[int],
    ops: list[Callable[[int, int], int]],
    result: int,
    q: int,
) -> bool:
    if desired == result and q == len(lst) - 1:
        return True

    if result > desired or q == len(lst) - 1:
        return False

    for f in ops:
        if solve(desired, lst, ops, f(result, lst[q + 1]), q + 1) == True:
            return True

    return False


def part1(inp: list[str]) -> int:
    ops = [lambda x, y: x + y, lambda x, y: x * y]

    s = 0
    for line in inp:
        desired, lst = line.split(": ")
        desired = int(desired)
        lst = tuple(int(x) for x in lst.split())

        if solve(desired, lst, ops, lst[0], 0):
            s += desired

    return s


def part2(inp: list[str]) -> int:
    ops = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(f"{x}{y}")]

    s = 0
    for line in inp:
        desired, lst = line.split(": ")
        desired = int(desired)
        lst = tuple(int(x) for x in lst.split())

        if solve(desired, lst, ops, lst[0], 0):
            s += desired

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
