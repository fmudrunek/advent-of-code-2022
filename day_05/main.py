import re
from pathlib import Path
from queue import LifoQueue
from typing import List, Tuple


def solve_part_1(data: List[str]) -> str:
    (stacks, instructions) = _parse_data(data)
    for instruction in instructions:
        regexed = re.match("move ([0-9]*) from ([0-9]*) to ([0-9]*)", instruction)
        amount, from_stack, to_stack = [int(_) for _ in regexed.groups()]
        for _ in range(amount):
            value = stacks[from_stack - 1].get()
            stacks[to_stack - 1].put(value)

    return "".join([stack.get() for stack in stacks])


def solve_part_2(data: List[str]) -> int:
    (stacks, instructions) = _parse_data(data)
    for instruction in instructions:
        regexed = re.match("move ([0-9]*) from ([0-9]*) to ([0-9]*)", instruction)
        amount, from_stack, to_stack = [int(_) for _ in regexed.groups()]
        crane_buffer = LifoQueue(maxsize=amount)
        for _ in range(amount):
            crane_buffer.put(stacks[from_stack - 1].get())
        for _ in range(amount):
            stacks[to_stack - 1].put(crane_buffer.get())

    return "".join([stack.get() for stack in stacks])


def _parse_stacks(data: List[str]) -> List[LifoQueue]:
    column_count = int(data.pop().strip()[-1])
    stacks = [LifoQueue(maxsize=column_count * len(data)) for _ in range(column_count)]
    for line in reversed(data):
        for count, index in enumerate(range(1, len(line), 4)):
            element = line[index]
            if element != " ":
                stacks[count].put(element)

    return stacks


def _parse_data(data: List[str]) -> Tuple[List[LifoQueue], List[str]]:
    for index, line in enumerate(data):
        if line.strip() == "":
            return (_parse_stacks(data[0:index]), data[index + 1 :])


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.rstrip("\n") for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
