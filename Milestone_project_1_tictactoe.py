
import random

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("")

def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)  # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True
    return False

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    return ' ' not in board[1:]

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(input('Choose a position: (1-9) '))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return position

def replay():
    choice = input("Play again? Enter Yes or No: ").lower()
    return choice in ('yes', 'y')

print('Welcome to Tic Tac Toe!')

while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    game_on = input('Ready to play? Enter Y or N: ').lower().startswith('y')

    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
            position = player_choice(the_board) #removed turn from the function call
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie game!')
                game_on = False
            else:
                turn = 'Player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board) #removed turn from the function call
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie game!')
                game_on = False
            else:
                turn = 'Player 1'

    if not replay():
        break