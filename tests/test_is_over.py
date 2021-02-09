import pytest  # type: ignore
from typing import List
from engine import is_over

NUMBER_TO_WIN = 3
BOARD_SIZE = 25


@pytest.mark.parametrize(
    "board, done_move, sign, expected",
    [
        ([" " for _ in range(BOARD_SIZE)], 1, "O", False),
    ],
)
def test_is_over_row(
    board: List[str], done_move: int, sign: str, expected: bool
) -> None:
    assert is_over(board, done_move, sign) == expected
