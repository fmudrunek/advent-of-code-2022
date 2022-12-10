from collections import Counter
from pathlib import Path
from typing import List


def _get_first_marker(input: str, frame_size: int) -> int:
    counter = Counter()
    index = frame_size
    while index < len(input):
        sub_string = input[index - frame_size : index]
        counter.update(sub_string)
        if counter.most_common(1)[0][1] == 1:
            return index
        index += 1
        counter.clear()

    return -1


def solve_part_1(data: List[str]) -> int:
    return _get_first_marker(data[0], frame_size=4)


def solve_part_2(data: List[str]) -> int:
    return _get_first_marker(data[0], frame_size=14)


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
