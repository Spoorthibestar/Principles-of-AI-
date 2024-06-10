import random

def print_board(board):
    print(" -----------")
    for i in range(3):
        print(f"| {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print(" -----------")

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def computer_move(board):
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_positions)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    human_player = 'X'
    computer_player = 'O'

    while True:
        start = input("Who will play first? Enter 'H' for Human or 'C' for Computer: ").upper()

        if start == 'H':
            current_player = human_player
        elif start == 'C':
            current_player = computer_player
        else:
            print("Invalid input. Please enter 'H' or 'C'.")
            continue

        break

    print_board(board)

    while True:
        if current_player == human_player:
            move = input(f"Your turn, enter position (1-9): ")

            if move.isdigit() and 1 <= int(move) <= 9:
                index = int(move) - 1
                row = index // 3
                col = index % 3
                if board[row][col] == ' ':
                    board[row][col] = human_player
                    if check_winner(board):
                        print(f"You win!")
                        return
                    elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                        print("It's a tie!")
                        return
                    print_board(board)
                else:
                    print("That position is already taken. Try again.")
            else:
                print("Invalid input. Enter a number from 1 to 9.")

            current_player = computer_player

        else:  # Computer's turn
            row, col = computer_move(board)
            board[row][col] = computer_player
            print(f"Computer's turn: {row*3+col+1}")
            if check_winner(board):
                print("Computer wins!")
                return
            elif all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print("It's a tie!")
                return

            print_board(board)
            current_player = human_player

if __name__ == "__main__":
    tic_tac_toe()
