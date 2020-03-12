# author:       Luis Hauenstein
# email:        luishauenstein[at]gmail.com
# version:      1.0
# last update:  yyyymmdd 20200301


# PYTHON SCRIPT FOR IMPROVING YOUR TACTICAL VISION AT CHESS
# Concept can be found here:
# https://www.chess.com/article/view/improving-your-tactical-vision
#
#
# INFO ABOUT PYTHON CHESS LIBRARY:
# https://python-chess.readthedocs.io/
# https://python-chess.readthedocs.io/en/latest/core.html



# ***** beginning *****

import chess
from random import randint


print('Welcome to the tactical vision chess trainer! Please set a difficulty level, input "h" for help or press enter to exit.')
while True: #eternal loop
    #user chooses level and gamemode
    knightmode = False
    while True:
        print('')
        level = input()
        print('')
        try:
            #if level is int between 1 and 32, proceed to random number generator
            level = int(level)
            if level < 33 and level > 0:
                break
            else:
                print('The max level is 32 and the min level 1! Try again:')
        except:
            #if level is h, display rules
            if level == 'h':
                print('***** RULES *****')
                print('')
                print('Set a difficulty level between 1 and 32.\nA random piece will be placed on a random sqare of the board for every level of difficulty.')
                print('')
                print('You will be given the position of every piece in algebraic chess notation.\nYour job is to find every possible move every piece can make.')
                print('')
                print('You also have the choice to play Knight mode. In this gamemode every piece is a knight.\nYou can enter Knight mode by typing "n".')
                print('')
                print('You got the rules? Then set your difficulty level now:')
            #if level is n enter Knigh mode
            elif level =='n':
                knightmode = True
                print('Welcome to the Knight mode! In this mode, the pieces are Knights only.\nOn which difficulty do you want to play?')
            #if prompt is empty, exit
            elif level == '':
                exit()
            else:
                print('Not a valid input, try again. Input "h" for help or press enter to exit.')


    squares = [None] * level
    pieces = [None] * level
    position = [None] * level
    for i in range(level): #generate pieces
        if knightmode == False: #if not in knightmode pieces are random
            pieces[i] = randint(2,6)
        else: # if in knightmode pieces are all knights
            pieces[i] = 2

    #generate random positions
    while True:
        for i in range(level): #random squares
            squares[i] = randint(0,63)
        if level == len(set(squares)): #make sure that no pieces are on the same square
            break

    #printing position of pieces in algebraic notation
    print('Following pieces are on the board:')
    print('')
    for i in range(level):
        piece = chess.piece_symbol(pieces[i]).upper()
        file = chess.FILE_NAMES[chess.square_file(squares[i])]
        rank = chess.RANK_NAMES[chess.square_rank(squares[i])]
        algebraic = piece + file + rank
        print(algebraic)
    print('')

    #setting up board and pieces
    board = chess.Board()
    board.clear()
    for i in range(level):
        #  set piece method:
        #  set_piece_at(square: int, piece: Optional[chess.Piece], promoted: bool = False)
        #  sets a piece at the given square.
        board.set_piece_at(square = squares[i], piece = chess.Piece(pieces[i], True))
    #print(board) #for debugging


    #identifying legal moves
    legalmovesobject = board.legal_moves  # is same as chess.LegalMoveGenerator(board)
    legalmovesstring = str(legalmovesobject).split('(')[1].split(')')[0] # makes the object printline a comma seperated string
    legalmovesstring = legalmovesstring.replace(',','') #removes commas
    legalmoves = legalmovesstring.split(' ')#creates a list of possible moves
    #print(legalmoves) #for debugging

    #let user input moves, collect wrong inputs in lists
    x = '*'
    remaining = legalmoves[:]
    wronginputs = []
    print('Input a move which is possible in this position and press enter. Use the algebraic notation.\nIf a square can be reached by multiple pieces, remember to input all moves. \nRepeat until you think you got all possible moves. Then press enter again.')
    print('')
    while x != '':
        x = input().strip()
        try:
            remaining.remove(x)
        except:
            if x not in legalmoves:
                wronginputs.append(x)
    wronginputs.remove('')

    #check if user got everything right and print mistakes
    print('')
    if len(remaining) == 0:
        print('Congrats! You found every possible move in this position!')
    else:
        print('Yikes! Looks like you missed some possible moves:')
        print('')
        for i in remaining:
            print(i)

    if len(wronginputs) != 0: # if there are wrong inputs, print them
        print('')
        print('Following inputs were no legal moves:')
        print('')
        for i in wronginputs:
            print(i)
    print('')
    print('Here is how the board in this game looks:')
    print('')
    print(board)
    print('')
    print('Do you want to play again? Input the difficulty, "h" for help or press enter to exit.')

# ***** end *****
