from pathlib import Path
from typing import List, Tuple


def _parse_line(line: str) -> List[int]:
    range1, range2 = line.split(",")
    r1min, r1max = [int(num) for num in range1.split("-")]
    r2min, r2max = [int(num) for num in range2.split("-")]
    return [r1min, r1max, r2min, r2max]

def solve_part_1(data: List[str]) ->  int:
    counter = 0
    for line in data:
        r1min, r1max, r2min, r2max = _parse_line(line)
        if (r1min >= r2min and r1max <= r2max) or (r2min >= r1min and r2max <= r1max):
            counter += 1

    return counter


def solve_part_2(data: List[str]) -> int:
    counter = 0
    for line in data:
        r1min, r1max, r2min, r2max = _parse_line(line)
        if (r2min <= r1min <= r2max) or (r2min <= r1max <= r2max) or (r1min <= r2min <= r1max) or (r1min <= r2max <= r1max):
            counter += 1

    return counter



def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]

if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")

