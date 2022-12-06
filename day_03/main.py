from pathlib import Path
from typing import List
from more_itertools import chunked

def _char_to_int(letter: str) -> int:
    if (letter.isupper()):
        return ord(letter) - 38
    return ord(letter) - 96

def solve_part_1(data: List[str]) ->  int:
    result = 0
    for line in data:
        compartment1, compartment2 = line[:len(line)//2], line[len(line)//2:]

        intersection = set(compartment1).intersection(set(compartment2)).pop()
        result += _char_to_int(intersection)

    return result


def solve_part_2(data: List[str]) -> int:
    result = 0
    for chunked_lines in chunked(data, 3):
        intersection = set(chunked_lines[0]).intersection(set(chunked_lines[1]), set(chunked_lines[2])).pop()
        result += _char_to_int(intersection)

    return result



def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]

if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")

