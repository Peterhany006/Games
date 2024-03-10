# File: CS112_A1_T6_20230101.py
# Purpose: connect 4
# Author: Peter Hany Rufeat shaker
# ID: 20230101

def print_board(board):
    #This function prints the current state of the game board. It prints each row of the board, showing the status of each cell.
    for row in board:
        print("|", end="")
        for cell in row:
            print(cell, end="|")
        print()
    print("-" * (len(board[0]) * 2 + 1))
    print(" ", end="")
    for col in range(1, len(board[0]) + 1):
        print(col, end=" ")
    print()
def check_win(board, player):#This function checks if the current player has won the game. It checks for horizontal, vertical, and both diagonal wins.
    # Check horizontally
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row][col+i] == player for i in range(4)):
                return True
    # Check vertically
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row+i][col] == player for i in range(4)):
                return True
    # Check diagonally (positive slope)
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row+i][col+i] == player for i in range(4)):
                return True
    # Check diagonally (negative slope)
    for row in range(len(board) - 3):
        for col in range(3, len(board[0])):
            if all(board[row+i][col-i] == player for i in range(4)):
                return True
    return False
def check_full(board):# This function checks if the board is completely filled without a winner, resulting in a tie.
    for row in board:
        if ' ' in row:
            return False
    return True
def is_valid_move(board, col):
    #This function checks if the move requested by the player is valid, meaning they can place their token in the specified column.
    return 0 <= col < len(board[0]) and board[0][col] == ' '
def make_move(board, col, player):# This function places the player's token in the specified column.
    for row in range(len(board)-1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return
def main():
    #This is the function that executes the entire game. It initializes the board with specified dimensions and starts the game loop, alternating between players and checking for wins or ties.
    rows = 6
    cols = 7
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    current_player = 'X'
    while True:
        print_board(board)
        while True:# Get player input
            try:
                col = int(input(f"Player {current_player}, enter column (1-{cols}): ")) - 1
                if is_valid_move(board, col):
                    break
                else:
                    print("Invalid move. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        make_move(board, col, current_player)
        if check_win(board, current_player):# Check for win
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_full(board):# Check for tie
            print_board(board)
            print("It's a tie!")
            break
        current_player = 'O' if current_player == 'X' else 'X'
        # Switch player
if __name__ == "__main__":
    main()
