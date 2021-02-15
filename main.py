# ------- Global Variables ----------

# Game board
board = [
    "-", "-", "-",
    "-", "-", "-",
    "-", "-", "-",
]

# If game is still going
game_still_going = True

# Who won? or tie?
winner = None

# Whos turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    # display initial board
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # Set up global vairables
    global winner
    global game_still_going

    # check rows
    if (board[0] == board[1] == board[2] != "-"):
        winner = board[0]
    elif (board[3] == board[4] == board[5] != "-"):
        winner = board[3]
    elif (board[6] == board[7] == board[8] != "-"):
        winner = board[6]
    # check columns
    elif (board[0] == board[3] == board[6] != "-"):
        winner = board[0]
    elif (board[1] == board[4] == board[7] != "-"):
        winner = board[1]
    elif (board[2] == board[5] == board[8] != "-"):
        winner = board[2]
    # check diagonals
    elif (board[0] == board[4] == board[8] != "-"):
        winner = board[0]
    elif (board[2] == board[4] == board[6] != "-"):
        winner = board[2]

    if (winner != None): 
        game_still_going = False
    return


def check_if_tie():
    # Set up global vairables
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    return


play_game()
