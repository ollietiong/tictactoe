"""
Tic Tac Toe Player
"""

import math
import copy

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
    count_x = 0
    count_y = 0
    for row in board:
        for item in row:
            if item == 'X':
                count_x +=1
            elif item == 'O':
                count_y +=1
    
    if count_x > count_y:
        return O
    elif count_x == count_y:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for idx, row in enumerate(board):
        for ix,item in enumerate(row):
            if item == None:
                actions_set.add((idx,ix))
    
    return actions_set

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    if board_copy[action[0]][action[1]] != None:
        raise Exception
    else:
        board_copy[action[0]][action[1]] = player(board_copy)
    
    return board_copy

def winner(board):
    
    winner = None
    # check horiz 
    for row in board:
        if row[0] != None:
            row_it = iter(row)
            player = next(row_it)
            if next(row_it) == player:
                if next(row_it) == player:
                    winner = player

    # check vertical 
    for idx,item in enumerate(board[0]):
        if item != None:
            player = item
            if board[1][idx] == player:
                if board[2][idx] == player:
                    winner = player

    # check diagonal (only need check central point as a starting point, there are only 2 possible diagonals)
    centre_point = board[1][1] 
    if board[0][0]== centre_point and board[2][2] == centre_point:
        winner= centre_point
    if board[0][2]== centre_point and board[2][0] == centre_point:
        winner = centre_point

    return(winner)


def terminal(board):
    terminal = True
    # check winner
    if winner(board) == None: # check board not full
        for row in board:
            for item in row:
                if item == None:
                    terminal = False
    return(terminal)



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == 'X':
        return 1
    elif winning_player == 'O':
        return -1
    else:
        return 0
    
global alpha 
alpha = - math.inf
global beta 
beta = math.inf    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
    def max_value(board,alpha,beta):
        if terminal(board) == True:
            return utility(board)
        v =  -math.inf
        for action in actions(board):
            v = max(v,min_value(result(board,action),alpha,beta))
            alpha= max(alpha,v)
            if beta <= alpha:
                break
        return v

    def min_value(board,alpha,beta):
        if terminal(board) == True:
            return utility(board)
        v = math.inf
        for action in actions(board):
            v = min(v,max_value(result(board,action),alpha, beta))
            beta = min(beta,v)
            if beta <= alpha:
                break
        return v


    # check terminal board
    
    if terminal(board) == True:
        print("Minimax call")
        return None
    else:
        # check player
        c_player = player(board)
        if c_player == 'X': # i.e MAX player
            actions_values = {}
            
            for action in actions(board):
                value = min_value(result(board,action), alpha, beta)

                actions_values.update({action:value})
            return(max(actions_values, key=actions_values.get))
        else: # i.e MIN PLAYER
            actions_values = {}
            for action in actions(board):
                value = max_value(result(board,action),alpha,beta)
                actions_values.update({action: value})
            #print(actions_values)
            return(min(actions_values, key=actions_values.get))



