from copy import deepcopy
from enum import Enum

DAY = 6


class Direction(Enum):
    N = (-1, 0)
    E = (0, 1)
    S = (1, 0)
    W = (0, -1)


OBSTACLE = 1
DIRECTION_TO_90 = {
    Direction.N: Direction.E,
    Direction.E: Direction.S,
    Direction.S: Direction.W,
    Direction.W: Direction.N,
}


def is_ok(M: list[list[int]], i: int, j: int) -> bool:
    if i < 0 or j < 0:
        return False
    if i >= len(M) or j >= len(M[i]):
        return False
    return True


def parse_input(inp: list[str]) -> tuple[list[list[int]], tuple[int]]:
    M = [[0 for _ in range(len(inp))] for _ in range(len(inp[0]))]

    Gi, Gj = (-1, -1)

    for i in range(len(M)):
        for j in range(len(M[i])):
            if inp[i][j] == "^":
                Gi, Gj = (i, j)
                M[i][j] = [Direction.N]
            elif inp[i][j] == "#":
                M[i][j] = OBSTACLE

    return M, (Gi, Gj)


def part1(inp: list[str]) -> int:
    M, (Gi, Gj) = parse_input(inp)
    direction = Direction.N

    if (Gi, Gj) == (-1, -1):
        return 0

    i2, j2 = Gi + direction.value[0], Gj + direction.value[1]
    while is_ok(M, i2, j2):
        if M[i2][j2] == OBSTACLE:
            direction = DIRECTION_TO_90[direction]
            i2, j2 = Gi, Gj
        elif type(M[i2][j2]) == list:
            M[i2][j2].append(direction)
        else:
            M[i2][j2] = [direction]
        Gi, Gj = i2, j2
        i2, j2 = i2 + direction.value[0], j2 + direction.value[1]

    c = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if type(M[i][j]) == list:
                c += 1
    return c


def part2(inp: list[str]) -> int:
    M0, (Gi0, Gj0) = parse_input(inp)

    def test_timeline(Gi: int, Gj: int, Oi: int, Oj: int) -> bool:
        M = deepcopy(M0)
        M[Oi][Oj] = OBSTACLE
        direction = Direction.N

        if (Gi, Gj) == (-1, -1):
            return 0

        i2, j2 = Gi + direction.value[0], Gj + direction.value[1]
        while is_ok(M, i2, j2):
            if M[i2][j2] == OBSTACLE:
                direction = DIRECTION_TO_90[direction]
                i2, j2 = Gi, Gj
            elif type(M[i2][j2]) == list:
                if direction in M[i2][j2]:
                    return True
                M[i2][j2].append(direction)
            else:
                M[i2][j2] = [direction]
            Gi, Gj = i2, j2
            i2, j2 = i2 + direction.value[0], j2 + direction.value[1]

        return False

    c = 0
    for i in range(len(M0)):
        for j in range(len(M0[i])):
            if (
                (i, j) != (Gi0, Gj0)
                and M0[i][j] != OBSTACLE
                and test_timeline(Gi0, Gj0, i, j)
            ):
                c += 1
    return c


def read_input_file(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf8") as fin:
        inp = fin.readlines()

    return [line.strip() for line in inp]


if __name__ == "__main__":
    input_str = read_input_file(f"data/input{DAY:02d}.txt")
    # input_str = read_input_file(f"data/input00.txt")

    print(f"Part 1: {part1(input_str)}")
    print(f"Part 2: {part2(input_str)}")
