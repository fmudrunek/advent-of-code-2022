import itertools
from pathlib import Path
from typing import List, Tuple


def _create_grid(data: List[str]) -> List[List[int]]:
    return [[int(num) for num in line] for line in data]


def _tree_is_visible(tree_index: Tuple[int, int], grid: List[List[int]]) -> bool:
    tree_height = grid[tree_index[0]][tree_index[1]]

    blocked = False
    for index in reversed(range(0, tree_index[1])):
        if grid[tree_index[0]][index] >= tree_height:
            blocked = True
            break

    if not blocked:
        return True

    blocked = False
    for index in reversed(range(tree_index[1] + 1, len(grid[0]))):
        if grid[tree_index[0]][index] >= tree_height:
            blocked = True
            break

    if not blocked:
        return True

    blocked = False
    for index in reversed(range(0, tree_index[0])):
        if grid[index][tree_index[1]] >= tree_height:
            blocked = True
            break

    if not blocked:
        return True

    blocked = False
    for index in reversed(range(tree_index[0] + 1, len(grid))):
        if grid[index][tree_index[1]] >= tree_height:
            blocked = True
            break

    return not blocked


def _tree_scenic_score(tree_index: Tuple[int, int], grid: List[List[int]]) -> int:
    tree_height = grid[tree_index[0]][tree_index[1]]

    left_score = 0
    for index in reversed(range(0, tree_index[1])):
        left_score += 1
        if grid[tree_index[0]][index] >= tree_height:
            break

    right_score = 0
    for index in range(tree_index[1] + 1, len(grid[0])):
        right_score += 1
        if grid[tree_index[0]][index] >= tree_height:
            break

    up_score = 0
    for index in reversed(range(0, tree_index[0])):
        up_score += 1
        if grid[index][tree_index[1]] >= tree_height:
            break

    down_score = 0
    for index in range(tree_index[0] + 1, len(grid)):
        down_score += 1
        if grid[index][tree_index[1]] >= tree_height:
            break

    return left_score * right_score * up_score * down_score


def solve_part_1(data: List[str]) -> int:
    grid = _create_grid(data)
    width = len(grid[0])
    height = len(grid)

    visible_count = 2 * width + 2 * height - 4

    for i, j in itertools.product(range(1, width - 1), range(1, height - 1)):
        if _tree_is_visible((i, j), grid):
            visible_count += 1

    return visible_count


def solve_part_2(data: List[str]) -> int:
    grid = _create_grid(data)
    width = len(grid[0])
    height = len(grid)

    highest = 0
    for i, j in itertools.product(range(0, width - 1), range(0, height - 1)):
        scenic_score = _tree_scenic_score((i, j), grid)
        if scenic_score > highest:
            highest = scenic_score

    return highest


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
