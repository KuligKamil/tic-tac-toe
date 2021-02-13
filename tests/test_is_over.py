from typing import List

import pytest  # type: ignore

from engine import is_over

NUMBER_TO_WIN = 3
BOARD_SIZE = 16

EMPTY_BOARD = [" " for _ in range(BOARD_SIZE)]


@pytest.mark.parametrize(
    "board, done_move, sign, expected",
    [
        (EMPTY_BOARD, 1, "O", False),
        (['O', 'O', 'O', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         1, "O", True),
        ([' ', ' ', 'O', 'O',
          'O', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         3, "O", False),
        ([' ', ' ', 'O', 'O',
          'O', 'O', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         3, "O", False),
        ([' ', ' ', 'O', 'O',
          ' ', 'O', 'O', 'O',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         5, "O", True),

    ]
)
def test_is_over_row(board: List[str], done_move: int, sign: str, expected: bool) -> None:
    assert is_over(board, done_move, sign) == expected


@pytest.mark.parametrize(
    "board, done_move, sign, expected",
    [
        (EMPTY_BOARD, 1, "O", False),
        (['O', ' ', ' ', ' ',
          'O', ' ', ' ', ' ',
          'O', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         0, "O", True),
        (['O', 'O', ' ', ' ',
          'O', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         1, "O", False),
        ([' ', ' ', ' ', ' ',
          ' ', ' ', 'O', ' ',
          ' ', ' ', 'O', ' ',
          ' ', ' ', 'O', ' ',
          ' ', ' ', ' ', ' '],
         6, "O", True),
    ]
)
def test_is_over_column(board: List[str], done_move: int, sign: str, expected: bool) -> None:
    assert is_over(board, done_move, sign) == expected


@pytest.mark.parametrize(
    "board, done_move, sign, expected",
    [
        (EMPTY_BOARD, 1, "O", False),
        (['O', ' ', ' ', ' ',
          ' ', 'O', ' ', ' ',
          ' ', ' ', 'O', ' ',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         0, "O", True),
        ([' ', 'O', ' ', ' ',
          ' ', ' ', 'O', ' ',
          ' ', ' ', ' ', 'O',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         1, "O", True),
        ([' ', ' ', ' ', ' ',
          ' ', ' ', 'O', ' ',
          ' ', ' ', ' ', 'O',
          ' ', ' ', ' ', ' ',
          ' ', ' ', ' ', ' '],
         6, "O", False),
        ([' ', ' ', ' ', ' ',
          'O', ' ', 'O', ' ',
          ' ', 'O', ' ', 'O',
          ' ', ' ', 'O', ' '],
         9, "O", True),
    ]
)
def test_diagonal_left(board: List[str], done_move: int, sign: str, expected: bool) -> None:
    assert is_over(board, done_move, sign) == expected
