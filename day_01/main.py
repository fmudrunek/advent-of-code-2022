from pathlib import Path
from typing import List

def _load_elves(data: List[str]) -> List[int]:
    result = []
    current_elf_sum = 0
    for line in data:
        if len(line.strip()) == 0:
            result.append(current_elf_sum)
            current_elf_sum = 0
        else:
            current_elf_sum += int(line)
    result.append(current_elf_sum)
    
    return sorted(result)




def solve_part_1(data: List[str]) ->  int:
    return _load_elves(data)[-1]

def solve_part_2(data: List[str]) -> int:
    return sum(_load_elves(data)[-3:])





def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]

if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")

