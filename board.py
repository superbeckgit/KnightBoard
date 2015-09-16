#!/home/mbeck/anaconda/bin/python
# -*- coding: utf-8 -*-
r"""
Knight board program:
    validates knight moves
    finds shortest path from start to end
    finds longest path from start to end
    accepts board layouts with penalty terrain

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
    . . . . . . . . B . . . L L L . . . . . . . . . . . . . . . . .
    . . . . . . . . B . . . L L L . . . . . . . . . . . . . . . . .
    . . . . . . . . B . . . L L L . . . L L L . . . . . . . . . . .
    . . . . . . . . B . . . L L L . . L L L . . . R R . . . . . . .
    . . . . . . . . B . . . L L L L L L L L . . . R R . . . . . . .
    . . . . . . . . B . . . L L L L L L . . . . . . . . . . . . . .
    . . . . . . . . B . . . . . . . . . . . . R R . . . . . . . . .
    . . . . . . . . B B . . . . . . . . . . . R R . . . . . . . . .
    . . . . . . . . W B B . . . . . . . . . . . . . . . . . . . . .
    . . . R R . . . W W B B B B B B B B B B . . . . . . . . . . . .
    . . . R R . . . W W . . . . . . . . . B . . . . . . . . . . . .
    . . . . . . . . W W . . . . . . . . . B . . . . . . T . . . . .
    . . . W W W W W W W . . . . . . . . . B . . . . . . . . . . . .
    . . . W W W W W W W . . . . . . . . . B . . R R . . . . . . . .
    . . . W W . . . . . . . . . . B B B B B . . R R . W W W W W W W
    . . . W W . . . . . . . . . . B . . . . . . . . . W . . . . . .
    W W W W . . . . . . . . . . . B . . . W W W W W W W . . . . . .
    . . . W W W W W W W . . . . . B . . . . . . . . . . . . B B B B
    . . . W W W W W W W . . . . . B B B . . . . . . . . . . B . . .
    . . . W W W W W W W . . . . . . . B W W W W W W B B B B B . . .
    . . . W W W W W W W . . . . . . . B W W W W W W B . . . . . . .
    . . . . . . . . . . . B B B . . . . . . . . . . B B . . . . . .
    . . . . . R R . . . . B . . . . . . . . . . . . . B . . . . . .
    . . . . . R R . . . . B . . . . . . . . . . . . . B . T . . . .
    . . . . . . . . . . . B . . . . . R R . . . . . . B . . . . . .
    . . . . . . . . . . . B . . . . . R R . . . . . . . . . . . . .
    . . . . . . . . . . . B . . . . . . . . . . R R . . . . . . . .
    . . . . . . . . . . . B . . . . . . . . . . R R . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .  # The last four rows originally missing
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Level 5 [HARD]: Compute the longest sequence of moves to complete Level 3 without
    visiting the same square twice.  Use the 32x32 board.
"""


#%% imports
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import doctest
import numpy as np
import copy


#%% GLOBALS
CHAR_DICT = {'.':0, 'S':1, 'E':2, 'K':3, 'W':4, 'R':5, 'B':6, 'T':7, 'L':8, 'x': 9}
VALU_DICT = {value:key for (key,value) in CHAR_DICT.items()}
SMALL_BOARD_CHAR = r"""
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
"""
LARGE_BOARD_CHAR = r"""
. . . . . . . . B . . . L L L . . . . . . . . . . . . . . . . .
. . . . . . . . B . . . L L L . . . . . . . . . . . . . . . . .
. . . . . . . . B . . . L L L . . . L L L . . . . . . . . . . .
. . . . . . . . B . . . L L L . . L L L . . . R R . . . . . . .
. . . . . . . . B . . . L L L L L L L L . . . R R . . . . . . .
. . . . . . . . B . . . L L L L L L . . . . . . . . . . . . . .
. . . . . . . . B . . . . . . . . . . . . R R . . . . . . . . .
. . . . . . . . B B . . . . . . . . . . . R R . . . . . . . . .
. . . . . . . . W B B . . . . . . . . . . . . . . . . . . . . .
. . . R R . . . W W B B B B B B B B B B . . . . . . . . . . . .
. . . R R . . . W W . . . . . . . . . B . . . . . . . . . . . .
. . . . . . . . W W . . . . . . . . . B . . . . . . T . . . . .
. . . W W W W W W W . . . . . . . . . B . . . . . . . . . . . .
. . . W W W W W W W . . . . . . . . . B . . R R . . . . . . . .
. . . W W . . . . . . . . . . B B B B B . . R R . W W W W W W W
. . . W W . . . . . . . . . . B . . . . . . . . . W . . . . . .
W W W W . . . . . . . . . . . B . . . W W W W W W W . . . . . .
. . . W W W W W W W . . . . . B . . . . . . . . . . . . B B B B
. . . W W W W W W W . . . . . B B B . . . . . . . . . . B . . .
. . . W W W W W W W . . . . . . . B W W W W W W B B B B B . . .
. . . W W W W W W W . . . . . . . B W W W W W W B . . . . . . .
. . . . . . . . . . . B B B . . . . . . . . . . B B . . . . . .
. . . . . R R . . . . B . . . . . . . . . . . . . B . . . . . .
. . . . . R R . . . . B . . . . . . . . . . . . . B . T . . . .
. . . . . . . . . . . B . . . . . R R . . . . . . B . . . . . .
. . . . . . . . . . . B . . . . . R R . . . . . . . . . . . . .
. . . . . . . . . . . B . . . . . . . . . . R R . . . . . . . .
. . . . . . . . . . . B . . . . . . . . . . R R . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
"""



#%% Class definitions
class Board():
    r"""
    Board class

    Attributes
    ----------
    map
    nCols
    nRows
    original

    """

    def __init__(self, layout):
        r"""
        Initialize board layout

        Paremeters
        ----------
        layout : (A,B) ndarray

        Examples
        --------
        test with the small board layout
        >>> myboard = Board(SMALL_BOARD_CHAR)

        """
        # split into rows
        lines = layout.strip().split('\n')
        # remove empty rows
        lines = [thisline for thisline in lines if thisline]
        # preallocate map np array
        self.nRows = len(lines)
        self.nCols = len(lines[0].split())
        self.map = np.zeros((self.nRows,self.nCols),dtype=int)
        # fill the map, x is vertical (down), y is horizontal (right)
        for x, thisline in enumerate(lines):
            for y, thischar in enumerate(thisline.split()):
                self.map[x,y] = CHAR_DICT[thischar]
        self.original = copy.deepcopy(self.map)

    def validate_position(self, position):
        r"""
        Determines if position is within board bounds

        Parameters
        ----------
        position : (1,2) ndarray integer
            desired board coordinates

        Returns
        -------
        bool
            True if within board, False if outside board

        Examples
        --------

        >>> myboard = Board(SMALL_BOARD_CHAR)
        >>> pos = np.array((1,2))
        >>> myboard.validate_position(pos)
        (True, 0)

        """
        penalty = 0
        (x, y)  = position
        if (x >= 0) & (x < self.nCols):
            if (y >= 0) & (y < self.nRows):
                if self.map[x, y] not in {CHAR_DICT['R'], CHAR_DICT['B'],\
                                              CHAR_DICT['K'], CHAR_DICT['x']}:
                    # square can be occupied, determine move penalty
                    if self.map[x, y] == CHAR_DICT['W']:
                        penalty = 1
                    elif self.map[x, y] == CHAR_DICT['L']:
                        penalty = 4
                    else:
                        # no penalty for normal squares or teleports
                        return True, penalty
                else:
                    # terrain cannot be occupied
                    return False, penalty
            else:
                # invalid y coordinate
                return False, penalty
        else:
            # invalid x coordinate
            return False, penalty

    def display(self, original=False):
        r""" Prints the map to the command prompt

        Examples
        --------
        test with the small board layout
        >>> myboard = Board(SMALL_BOARD_CHAR);
        >>> myboard.display()
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .
        . . . . . . . .

        """
        if original:
            map = self.original
        else:
            map = self.map
        for row in map:
            for ix, each in enumerate(row):
                # add pad space character except on last character
                if ix != len(row)-1:
                    pad = ' '
                else:
                    pad = ''
                print(VALU_DICT[each] + pad, end='')
            # finished the line, print line return
            print('')


if __name__ == '__main__':
    doctest.testmod(verbose=False)
    myboard = Board(LARGE_BOARD_CHAR)
    myboard.display()

