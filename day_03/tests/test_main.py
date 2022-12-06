from pathlib import Path
from ..main import solve_part_1, solve_part_2

def test_solve_part_1():
    input_path = input_path = Path(__file__).parent / "test_data_1.txt"
    expected = 157

    actual = solve_part_1(input_path)
    
    assert actual == expected 

def test_solve_part_2():
    input_path = input_path = Path(__file__).parent / "test_data_1.txt"
    expected = 70

    actual = solve_part_2(input_path)
    
    assert actual == expected 
