import dataclasses
from dataclasses import dataclass
from functools import reduce
from pathlib import Path
from typing import List


@dataclass(unsafe_hash=True)
class Point:
    x: int
    y: int


def _is_adjecent(a: Point, b: Point) -> bool:
    return abs(a.x - b.x) < 2 and abs(a.y - b.y) < 2


def _follow_move(lead: Point, follow: Point) -> Point:
    if _is_adjecent(lead, follow):
        return follow

    if lead.x > follow.x:
        follow.x += 1
    if lead.x < follow.x:
        follow.x -= 1

    if lead.y > follow.y:
        follow.y += 1
    if lead.y < follow.y:
        follow.y -= 1

    return follow


def _move_point(point: Point, direction: str) -> None:
    match direction:
        case "R":
            point.x += 1
        case "L":
            point.x -= 1
        case "U":
            point.y += 1
        case "D":
            point.y -= 1


def _solve(data: List[str], knot_count: int) -> int:
    knots = [Point(0, 0) for _ in range(knot_count)]
    visited_locations = [Point(0, 0)]

    for line in data:
        direction, count = line.split()
        amount = int(count)

        for _ in range(amount):
            _move_point(knots[0], direction)
            tail_previous = dataclasses.replace(knots[-1])
            reduce(_follow_move, knots)
            if knots[-1] != tail_previous:
                visited_locations.append(dataclasses.replace(knots[-1]))

    return len(set(visited_locations))


def solve_part_1(data: List[str]) -> int:
    return _solve(data, 2)


def solve_part_2(data: List[str]) -> int:
    return _solve(data, 10)


def get_data(path: Path) -> List[str]:
    with path.open() as input_file:
        return [line.strip() for line in input_file.readlines()]


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input_data.txt"
    data = get_data(input_path)
    result_part_1 = solve_part_1(data)
    result_part_2 = solve_part_2(data)
    print(f"Part 1 result: {result_part_1}\nPart 2 result: {result_part_2}")
