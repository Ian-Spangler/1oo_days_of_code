EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

WIN_COMBOS = [
    (0,1,2), (3,4,5), (6,7,8),  # rows
    (0,3,6), (1,4,7), (2,5,8),  # columns
    (0,4,8), (2,4,6)            # diagonals
]

def print_board(board):
    print()
    for r in range(3):
        row = " | ".join(board[3*r : 3*r+3])
        print(f" {row} ")
        if r < 2:
            print("---+---+---")
    print()

def available_moves(board):
    return [i for i, v in enumerate(board) if v == EMPTY]

def check_winner(board):
    for a, b, c in WIN_COMBOS:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "Draw"
    return None

def turn(board, symbol):
    while True:
        try:
            pos = int(input(f"Player {symbol} — Choose a position (1-9): ")) - 1
            if pos not in range(9):
                print("Please enter a number between 1 and 9.")
                continue
            if board[pos] != EMPTY:
                print("That spot is already taken. Choose another.")
                continue
            return pos
        except ValueError:
            print("Please enter a valid number (1-9).")

def play_game():
    board = [EMPTY] * 9
    current = PLAYER_X  

    print_board([str(i+1) for i in range(9)])
    print("Starting Tic-Tac-Toe! (Player vs Player)\n")

    while True:
        print_board(board)

        result = check_winner(board)
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"Winner: Player {result}")
            break

        move = turn(board, current)
        board[move] = current

        current = PLAYER_O if current == PLAYER_X else PLAYER_X

if __name__ == "__main__":
    play_game()
