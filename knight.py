# -*- coding: utf-8 -*-
r"""
GamePiece classes for KnightBoard project
    determines valid moves
    determines paths between start and end locations (min, max, first)

    Knight class

Written by Matt Beck Sept 2015

#%% Problem statement

[Knight Board]
The knight board can be represented in x,y coordinates.  The upper left position
is (0,0) and the bottom right is (7,7).  Assume there is a single knight chess
piece on the board that can move according to chess rules.  Sample S[tart] and
E[nd] points are shown below:
    . . . . . . . .
    . . . . . . . .
    . S . . . . . .
    . . . . . . . .
    . . . . . E . .
    . . . . . . . .
    . . . . . . . .
    . . . . . . . .
Level 1: Write a function that accepts a sequence of moves and reports
    whether the sequence contains only valid knight moves.  It should also
    optionally print the state of the knight board to the terminal as shown
    above after each move.  The current position should be marked with a 'K'.
Level 2: Compute a valid sequence of moves from a given start point to a given
    end point.
Level 3: Compute a valid sequence of moves from a given start point to a
    given end point in the fewest number of moves.
Level 4: Now repeat the Level 3 task for this 32x32 board.  Also, modify
    your validator from Level 1 to check your solutions.  This board has the
    following additional rules:
        1) W[ater] squares count as two moves when a piece lands there
        2) R[ock] squares cannot be used
        3) B[arrier] squares cannot be used AND cannot lie in the path
        4) T[eleport] squares instantly move you from one T to the other in
            the same move
        5) L[ava] squares count as five moves when a piece lands there
Level 5 [HARD]: Compute the longest sequence of moves to complete Level 3 without
    visiting the same square twice.  Use the 32x32 board.
"""


#%% imports
from __future__ import print_function
from __future__ import division
import doctest
import numpy as np


#%% GLOBALS
CHAR_DICT = {'.':0, 'S':1, 'E':2, 'K':3, 'W':4, 'R':5, 'B':6, 'T':7, 'L':8, 'x': 9}
VALU_DICT = {value:key for (key,value) in CHAR_DICT.items()}
SMALL_BOARD_CHAR = r"""
. . . . . . . .
. . . . . . . .
. S . . . . . .
. . . . . . . .
. . . . . E . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
"""


#%% Class definitions
class GamePiece():
    r""" GamePiece class """

    def __init__(self):
        r"""
        Initialize gamepiece on the board? TBD
        Specify valid moves list? TBD
        """
        self.valid_moves = {}



    def validate_move(self):
        r""" Check if passed in move sequence is valid """
        pass


class Knight(GamePiece):
    r""" Knight piece class """
    def __init__(self):
        self.valid_moves = {0:np.array((2, 1), dtype=int)}


if __name__ == '__main__':
    doctest.testmod(verbose=False)
    myboard = Board(LARGE_BOARD_CHAR)
    myboard.display()

