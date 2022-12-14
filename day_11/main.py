from __future__ import annotations

import re
from functools import reduce
from pathlib import Path
from queue import Queue
from typing import Callable, List


class Monkey:
    def __init__(
        self,
        items: Queue[int],
        operation: Callable[[int], int],
        test: Callable[[int, List[Monkey]], None],
    ) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.inspection_counter = 0

    def execute_action(
        self, monkeys: List[Monkey], worry_decreaser: Callable[[int], int]
    ) -> None:
        while not self.items.empty():
            item = self.items.get()
            worry_level = self.operation(item)
            new_worry = worry_decreaser(worry_level)
            self.test(new_worry, monkeys)
            self.inspection_counter += 1

    @staticmethod
    def create_monkey(data: List[str]) -> Monkey:
        if len(data) != 6:
            raise ValueError("Unexpected monkey input")
        items = [int(_) for _ in data[1].strip()[16:].split(",")]
        queue = Queue()
        for item in items:
            queue.put(item)

        operand, value = data[2][21:].split()
        operation_func = None
        match operand:
            case "*":
                operation_func = (lambda x: x * x) if value == "old" else (lambda x: x * int(value))
            case "+":
                operation_func = (lambda x: x + x) if value == "old" else (lambda x: x + int(value))

        divisable_by = int(data[3][18:])
        true_throw_to = int(data[4][24:])
        false_throw_to = int(data[5][25:])

        def throw_to_monkey(item: int, index: int, monkeys: List[Monkey]):
            monkeys[index].items.put(item)

        test_fc = (
            lambda item, monkey_list: throw_to_monkey(item, true_throw_to, monkey_list)
            if item % divisable_by == 0
            else throw_to_monkey(item, false_throw_to, monkey_list)
        )

        return Monkey(queue, operation_func, test_fc)


def _parse_monkeys(data: List[str]) -> List[Monkey]:
    monkeys = []
    for index in range(0, len(data), 7):
        monkeys.append(
            Monkey.create_monkey([_.strip() for _ in data[index : index + 6]])
        )
    return monkeys


def print_monkeys(monkeys: List[Monkey]) -> None:
    for index, monkey in enumerate(monkeys):
        print(f"Monkey {index}: {monkey.items.queue}")


def solve_part_1(data: List[str]) -> int:
    rounds = 20
    worry_decreaser = lambda worry_level: worry_level // 3
    monkeys = _parse_monkeys(data)
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.execute_action(monkeys, worry_decreaser)

    inspected_item_counts = sorted([monkey.inspection_counter for monkey in monkeys])
    return inspected_item_counts[-1] * inspected_item_counts[-2]


def _get_common_moddus(data: List[str]) -> int:
    divisors = re.findall("Test: divisible by (\d*)", "".join(data))
    return reduce(lambda x, y: x * y, [int(_) for _ in divisors])


def solve_part_2(data: List[str]) -> int:
    rounds = 10000
    modd = _get_common_moddus(data)
    worry_decreaser = lambda worry_level: worry_level % modd
    monkeys = _parse_monkeys(data)
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.execute_action(monkeys, worry_decreaser)

    inspected_item_counts = sorted([monkey.inspection_counter for monkey in monkeys])
    return inspected_item_counts[-1] * inspected_item_counts[-2]


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
