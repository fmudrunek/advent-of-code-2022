from pathlib import Path
from ..main import solve_part_1, solve_part_2, get_data

test_data = get_data(Path(__file__).parent / "test_data_1.txt")

def test_solve_part_1():
    actual = solve_part_1(test_data)
    assert actual == 15 

def test_solve_part_2():
    actual = solve_part_2(test_data)
    assert actual == 12