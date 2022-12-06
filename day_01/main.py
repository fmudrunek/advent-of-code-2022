from pathlib import Path
from typing import List

def _load_elves(input_path: Path) -> List[int]:
    result = []
    with input_path.open() as input_file:
        current_elf_sum = 0
        for line in input_file:
            if len(line.strip()) == 0:
                result.append(current_elf_sum)
                current_elf_sum = 0
            else:
                current_elf_sum += int(line)
        result.append(current_elf_sum)
    
    return sorted(result)




def solve_part_1(input_path: Path) ->  int:
    return _load_elves(input_path)[-1]

def solve_part_2(input_path: Path) -> int:
    return sum(_load_elves(input_path)[-3:])





if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    result_part_1 = solve_part_1(input_path)
    result_part_2 = solve_part_2(input_path)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")

