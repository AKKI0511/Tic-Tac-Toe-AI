"""
Tic Tac Toe Player
"""

import math

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
    num_x = 0
    num_o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_x = num_x + 1
            elif board[i][j] == O:
                num_o = num_o + 1

    if num_x == 0 and num_o == 0:
        return X
    elif num_x > num_o:
        return O
    elif num_x == num_o:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i, j))
    return acts


def result(board, action):
    p = player(board)
    changed_board = [row[:] for row in board]  # Use list comprehension for a copy

    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError()

    changed_board[i][j] = p
    return changed_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]

        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win is not None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def max_value(board):
    v = -100
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    v = 100
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    p = player(board)
    if p == X:
        v = -100
        output = (0, 0)
        for a in actions(board):
            if min_value(result(board, a)) > v:
                output = a
                v = min_value(result(board, a))
        b = result(board, output)
        return output
    else:
        v = 100
        output = (0, 0)
        for a in actions(board):
            if max_value(result(board, a)) < v:
                output = a
                v = max_value(result(board, a))
        b = result(board, output)
        return output
