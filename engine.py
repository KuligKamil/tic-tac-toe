from typing import List


def show_board(char: str) -> None:
    board: List = [char for _ in range(9)]
    print(
        f"""
       {board[0]} ┃ {board[1]} ┃ {board[2]}
     ━━━━╋━━━╋━━━━
       {board[3]} ┃ {board[4]} ┃ {board[5]}
     ━━━━╋━━━╋━━━━
       {board[6]} ┃ {board[7]} ┃ {board[8]}
    """
    )


if __name__ == "__main__":
    show_board("X")
    show_board("O")
