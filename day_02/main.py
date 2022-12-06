from pathlib import Path
from typing import Dict


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


def _solve(input_path: Path, scores: Dict[str, int]):
    result = 0
    with input_path.open() as input_file:
        for line in input_file:
            result += scores[line.strip()]
    return result



def solve_part_1(input_path: Path) ->  int:
    return _solve(input_path, _scores_1)


def solve_part_2(input_path: Path) -> int:
    return _solve(input_path, _scores_2)





if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    result_part_1 = solve_part_1(input_path)
    result_part_2 = solve_part_2(input_path)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")

