#!/usr/bin/env python


from IPython.display import clear_output

def display_board(board):


    print('' + board[7] + ' | ' +board[8]+ ' | ' + board[9])
    print('---------')
    print('' + board[4] + ' | ' +board[5]+ ' | ' + board[6])
    print('---------')
    print('' + board[1] + ' | ' +board[2]+ ' | ' + board[3])


#test_board = ['#','0','X','0','X','O','X','O','X','O','X']
#display_board(test_board)


def player_input():

    '''
    OUTPUT = (PLAYER 1 MARKER, PLAYER 2 MARKER)
    '''

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        
        return('X','O')
    else:
        return('O','X')

        









