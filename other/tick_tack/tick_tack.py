import random

board = [[" " for i in range(3)] for j in range(3)]

def draw_board():
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def get_human_move():
    while True:
        row = int(input("Enter row for your move: "))
        col = int(input("Enter col for your move: "))
        if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row][col] == " ":
            board[row][col] = "X"
            return
        print("Invalid move, try again.")

def get_ai_move():
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            return

def has_won(player):
    # check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # check columns
    for j in range(3):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    # check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def main():
    draw_board()
    while True:
        get_human_move()
        draw_board()
        if has_won("X"):
            print("You have won!")
            break
        get_ai_move()
        draw_board()
        if has_won("O"):
            print("AI has won!")
            break

main()