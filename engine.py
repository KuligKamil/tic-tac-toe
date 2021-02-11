import math
from typing import List

NUMBER_TO_WIN = 3
# min 3
# BOARD_SIZE = 9
BOARD_SIZE = 16
# BOARD_SIZE = 100
# BOARD_SIZE = 900
ROW_SIZE = int(math.sqrt(BOARD_SIZE))


def show_board(board: List) -> None:
    line = " "
    LINE = "━━━"
    ELEMENT = f"╋{LINE}"
    for index, value in enumerate(board):
        column_number = (index + 1) % ROW_SIZE
        if column_number == 1:
            line = f" {value} ┃ "
        elif column_number == 0:
            line = f"{line}{value}"
            print(line)
            if index != (BOARD_SIZE - 1):
                print(f"{LINE}{ELEMENT * (ROW_SIZE - 2)}╋{LINE}")
            line = ""
        else:
            line = f"{line}{value} ┃ "
    print()


def is_over(board: List[str], done_move: int, sign: str) -> bool:
    start, end = 0, ROW_SIZE - 1
    while end <= (BOARD_SIZE - 1):
        if sign * NUMBER_TO_WIN in ''.join(board[start:end]):
            return True
        start, end = start + ROW_SIZE, end + ROW_SIZE
    return False


if __name__ == "__main__":
    show_board([" " for _ in range(BOARD_SIZE)])
    show_board(["X" for _ in range(BOARD_SIZE)])
