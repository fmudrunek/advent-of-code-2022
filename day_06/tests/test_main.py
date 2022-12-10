from pathlib import Path

import pytest

from ..main import solve_part_1, solve_part_2


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_solve_part_1(input: str, expected_result: int):
    actual = solve_part_1([input])
    assert actual == expected_result


@pytest.mark.parametrize(
    "input, expected_result",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_solve_part_2(input: str, expected_result: int):
    actual = solve_part_2([input])
    assert actual == expected_result
