from pathlib import Path
from ..main import solve_part_1, solve_part_2

def test_solve_part_1():
    input_path = Path("tests/test_data_1.txt")
    expected = 24000

    actual = solve_part_1(input_path)
    
    assert actual == expected 

def test_solve_part_2():
    input_path = Path("tests/test_data_1.txt")
    expected = 45000

    actual = solve_part_2(input_path)
    
    assert actual == expected 
