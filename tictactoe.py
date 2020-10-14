# Tic-Tac-Toe Game

import os
import random
clear = lambda : os.system('cls')

def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    marker = ''
    # Asking Player 1 to choose X or O
    while marker != 'X' and marker != 'O':
        marker = input("Player 1, please choose X or O: ")

    # Assign marker to players
    # Output = (P_1 Marker, P_2 Marker)
    player1 = marker
    if player1 == 'X':
        return('X', 'O')
    else:
        return('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    # Win checking
    return((board[1] == board[2] == board[3] == mark) or    #bottom row
    (board[4] == board[5] == board[6] == mark) or   # middle row
    (board[7] == board[8] == board[9] == mark) or   # top row
    (board[1] == board[4] == board[7] == mark) or   # left column
    (board[2] == board[5] == board[8] == mark) or   # middle column
    (board[3] == board[6] == board[9] == mark) or   # right column
    (board[1] == board[5] == board[9] == mark) or   # diagonal
    (board[3] == board[5] == board[7])) # diagonal

def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if returns True
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Choose a position (1-9) : "))
    return position

def replay():
    choice = input("Play again? Yes / No? ")
    return choice == 'Yes'

print('Welcome to Tic-Tac-Toe Game...!!!')

# While loop to keep the game running...

while True:
    # Play the game
    ## Setup -> Board, Who's First, Choose Marker
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(str(turn) + ' will go first..')

    play_game = input('Ready to play? Y or N?')
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## Game Play
    while game_on:
        if turn == 'Player 1':
            # Show The Board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place marker in position
            place_marker(the_board, player1_marker, position)

            # Check if won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won the game..')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game is Tie..')
                    game_on = False
                else:
                    turn = 'Player 2'
        else:
            # Show The Board
            display_board(the_board)
            # Choose a position
            position = player_choice(the_board)
            # Place marker in position
            place_marker(the_board, player2_marker, position)

            # Check if won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won the game..')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Game is Tie..')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
    # Break out of while loop on replay()