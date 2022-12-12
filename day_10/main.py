from pathlib import Path
from typing import List


def solve_part_1(data: List[str]) -> int:
    cycle_counter = 0
    current_value = 1
    next_milestone = 20
    result = 0

    for line in data:
        if line == "noop":
            if cycle_counter + 1 == next_milestone:
                result += next_milestone * current_value
                next_milestone += 40
            cycle_counter += 1
        else:
            if cycle_counter + 2 >= next_milestone:
                result += next_milestone * current_value
                next_milestone += 40
            value = int(line.split()[1])
            cycle_counter += 2
            current_value += value

        if next_milestone > 220:
            break

    return result


class TheMachine:
    def __init__(self):
        self.sprite_position = 1
        self.crt_position = 0
        self.drawn_symbols = []

    def _draw(self):
        if abs(self.sprite_position - self.crt_position) <= 1:
            self.drawn_symbols.append("#")
        else:
            self.drawn_symbols.append(".")

        if self.crt_position == 39:
            self.crt_position = 0
            self.drawn_symbols.append("\n")
        else:
            self.crt_position += 1

    def do_noop(self) -> None:
        self._draw()

    def do_add(self, value: int) -> None:
        self._draw()
        self.sprite_position += value

    def get_result(self) -> str:
        return "".join(self.drawn_symbols)


def solve_part_2(data: List[str]) -> str:
    the_machine = TheMachine()
    for line in data:
        if line == "noop":
            the_machine.do_noop()
        else:
            value = int(line.split()[1])
            the_machine.do_noop()
            the_machine.do_add(value)

    return the_machine.get_result()


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
