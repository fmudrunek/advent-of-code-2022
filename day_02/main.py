from pathlib import Path
from typing import Dict, List

_scores_1 = {
    "A X": 4, "A Y": 8, "A Z": 3,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 7, "C Y": 2, "C Z": 6
}


_scores_2 = {
    "A X": 3, "A Y": 4, "A Z": 8,
    "B X": 1, "B Y": 5, "B Z": 9,
    "C X": 2, "C Y": 6, "C Z": 7
}


def _solve(data: List[str], scores: Dict[str, int]):
    result = 0
    for line in data:
        result += scores[line.strip()]
    return result


def solve_part_1(data: List[str]) -> int:
    return _solve(data, _scores_1)


def solve_part_2(data: List[str]) -> int:
    return _solve(data, _scores_2)


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
