from typing import List


def show_board(char):
    board: List = [char for i in range(9)]
    graphic = f"""
       {board[0]} ┃ {board[1]} ┃ {board[2]}
     ━━━━╋━━━╋━━━━
       {board[3]} ┃ {board[4]} ┃ {board[5]}
     ━━━━╋━━━╋━━━━
       {board[6]} ┃ {board[7]} ┃ {board[8]}
    """
    print(graphic)


if __name__ == "__main__":
    show_board("X")
    show_board("O")
