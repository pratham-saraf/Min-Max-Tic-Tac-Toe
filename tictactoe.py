"""
Tic Tac Toe Player
"""
import copy
from itertools import count
import math
from queue import Empty
import termios
from tkinter import N

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    movex =0
    moveO = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                movex +=1
            elif board[row][col] == O:
                moveO += 1
    if movex == moveO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possible.add((row,col))
    return possible        


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    (x , y) = action

    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        raise Exception("Invalid move")
    # create a copy of board

    boardtoreturn = copy.deepcopy(board)

    #play the move
    boardtoreturn[x][y] = player(board)

    return boardtoreturn

def checkhorver(board,symbol):
    for row in range(3):
        counth = 0
        for col in range(3):
            if board[row][col] == symbol:
                counth += 1
        if counth == 3:
            return True
    
    for col in range(3):
        countv = 0
        for row in range(3):

            if board[row][col] == symbol:
                countv += 1
        if countv ==3:
            return True
    
    return False

def checkdiag(board,symbol):
    countRTL = 0
    for row in range(3):
            if board[row][row]== symbol:
                countRTL +=1
    if countRTL ==3:
        return True
    
    count = 0
    for row in range(3):
        for col in range(3):

            if col == (3 - row -1):
                if board[row][col] == symbol:
                    count += 1
    if count ==3:
        return True
    
    return False



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if checkhorver(board,X) or checkdiag(board,X):
        return X
    elif checkdiag(board,O) or checkhorver(board,O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    return False
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_minimax(board):
    if terminal(board):
        return utility(board)
    v = float(-7886453467894653468769854645454)
    moves = actions(board)
    for move in moves:
        v= max(v,min_minimax(result(board,move)))
    return v

def min_minimax(board):
    if terminal(board):
        return utility(board)
    v = float(6546764674534689463165746548978)
    moves = actions(board)
    for move in moves:
        v = min(v,max_minimax(result(board,move)))
    return v

    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    chance = player(board)
    if terminal(board):
        return None
    elif chance == X:
        all_possible_soln=[]
        moves = actions(board)
        for move in moves:
            ans = min_minimax(result(board,move))
            all_possible_soln.append((ans,move))
        b = sorted(all_possible_soln,reverse=True)
        return b[0][1]
    elif chance == O:
        all_possible_soln=[]
        moves = actions(board)
        for move in moves:
            ans = max_minimax(result(board,move))
            all_possible_soln.append((ans,move))
        b = sorted(all_possible_soln)
        return b[0][1]
