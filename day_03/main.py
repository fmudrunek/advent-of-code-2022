from pathlib import Path


def _char_to_int(letter: str) -> int:
    if (letter.isupper()):
        return ord(letter) - 38
    return ord(letter) - 96

def solve_part_1(input_path: Path) ->  int:
    result = 0
    with input_path.open() as input_file:
        for line in input_file:
            stripped = line.strip()
            compartment1, compartment2 = stripped[:len(stripped)//2], stripped[len(stripped)//2:]

            intersection = set(compartment1).intersection(set(compartment2)).pop()
            result += _char_to_int(intersection)

    return result


def solve_part_2(input_path: Path) -> int:
    result = 0
    with input_path.open() as input_file:
        for line in input_file:
            stripped = line.strip()
            line2, line3 = next(input_file).strip(), next(input_file).strip()

            intersection = set(stripped).intersection(set(line2), set(line3)).pop()
            result += _char_to_int(intersection)

    return result





if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    result_part_1 = solve_part_1(input_path)
    result_part_2 = solve_part_2(input_path)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")

