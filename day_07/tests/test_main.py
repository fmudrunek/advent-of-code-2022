from pathlib import Path

from ..main import get_data, solve_part_1, solve_part_2

test_data = get_data(Path(__file__).parent / "test_data_1.txt")


def test_solve_part_1():
    actual = solve_part_1(test_data)
    assert actual == 95437


def test_solve_part_2():
    actual = solve_part_2(test_data)
    assert actual == 24933642
