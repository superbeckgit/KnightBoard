#!/home/mbeck/anaconda/bin/python
# -*- coding: utf-8 -*-
r"""
Knight class :
    validates knight moves
    finds shortest path from start to end
    finds longest path from start to end
    accepts board layouts with penalty terrain

Written by Matt Beck Sept 2015

"""

#%% imports
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import copy
import doctest
import numpy as np
import board


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


#%% Class definitions
class Knight():
    r""" Knight class

    """
    valid_moves = dict()
    valid_moves[0] = [(1, 0), (1, 0), (0, 1)]
    #. S .
    #. x .
    #. x E
    valid_moves[1] = [(1, 0), (1, 0), (0, -1)]
    #. S .
    #. x .
    #E x .
    valid_moves[2] = [(0, -1), (0, -1), (1, 0)]
    #. . .
    #x x S
    #E . .
    valid_moves[3] = [(0, -1), (0, -1), (-1, 0)]
    #E . .
    #x x S
    #. . .
    valid_moves[4] = [(-1, 0), (-1, 0), (0, -1)]
    #E x .
    #. x .
    #. S .
    valid_moves[5] = [(-1, 0), (-1, 0), (0, 1)]
    #. x E
    #. x .
    #. S .
    valid_moves[6] = [(0, 1), (0, 1), (-1, 0)]
    #. . E
    #S x x
    #. . .
    valid_moves[7] = [(0, 1), (0, 1), (1, 0)]
    #. . .
    #S x x
    #. . E


    def __init__(self, gboard, position):
        r"""
        Initialize board layout

        Paremeters
        ----------
        gboard   : board class object
        position : (1,2) ndarray
            starting position on the board

        Raises
        ------
        'invalid starting position' upon bad input

        Examples
        --------

        >>> myboard = board.Board(board.SMALL_BOARD_CHAR)
        >>> myknight = Knight(myboard, np.array((2,3)))

        """
        self.gboard = gboard
        # check that given start position is valid
        if gboard.validate_position(position):
            self.position = position
            (x, y)        = position
            gboard.map[x, y] = CHAR_DICT['K']
        else:
            raise Exception('invalid starting position')


    def validate_move(self, desired_move, **kargs):
        r""" Determine if move is valid

        Parameters
        ----------
        desired_move : enumerated integer
            index into self.valid_moves denoting move choice
        isstrict     : bool (optional)
            denotes if board.validate_position should use strict mode

        Returns
        -------
        cost    : int
            Total cost of move if executed
        isvalid : bool
            True if move is valid (allowed to happen)
        """
        # handle extra input
        bestrict = kargs.get('strict',False)
        move  = self.valid_moves[desired_move]
        # initialize move validity and cost
        isvalid = True
        cost    = 0
        test_pos = copy.deepcopy(self.position)
        myboard = self.gboard
        for ix, step in enumerate(move):
            test_pos += step
            if ix < len(move)-1:
                # get step validity for passover squares (ignore penalty)
                (step_v, _) = myboard.validate_position(test_pos, strict=bestrict)
            if ix == len(move)-1:
                # get step validity and penalty for landing square
                (step_v, step_p) = myboard.validate_position(test_pos, landing=True,
                                                             strict=bestrict)
                # add step penalty to move cost
                cost += step_p
            # combine step validity and move validity
            isvalid = isvalid & step_v
        # add standard move cost
        cost += 1
        return cost, isvalid

    def validate_sequence(self, movelist, **kargs):
        r"""
        Validate a sequence of moves for validity

        Parameters
        ----------
        movelist : [1xN] of int enums from {0:7} valid move list
        strict   : bool (otional)
            denotes if board.validate_position should use strict mode

        Returns
        -------
        totcost  : int
            Total cost of all moves if executed
        allvalid : bool
            True if all moves are valid (allowed to happen)

        """
        # handle extra input
        bestrict = kargs.get('strict',False)
        # initialize status vars
        allvalid = True
        totcost  = 0
        oldpos   = copy.deepcopy(self.position)
        oldmap   = copy.deepcopy(self.gboard.map)
        for each in movelist:
            #test the move
            (cost, isvalid) = self.validate_move(each, strict=bestrict)
            totcost  = cost + totcost
            allvalid = isvalid and allvalid
            if isvalid:
                # good move, execute it
                self.execute_move(each, strict=bestrict)
            else:
                # bad sequence
                totcost = 0
        # restore old self
        self.position = oldpos
        self.gboard.map = oldmap
        # all good moves
        return totcost, allvalid

    def execute_move(self, desired_move, **kargs):
        r"""
        Move the knight based on the move requested

        Parameters
        ----------
        desired_move : enumerated integer
            index into self.valid_moves denoting move choice
        **kargs      : dict
            capture strict settings to be passed through to validate_pos

        """
        # handle extra input
        bestrict = kargs.get('strict',False)
        # determine move validity and cost of move
        (cost, isvalid) = self.validate_move(desired_move, strict=bestrict)
        if isvalid:
            # get step list for move
            steplist = self.valid_moves[desired_move]
            # change the board layout to reflect the move
            cur_pos = copy.deepcopy(self.position)
            self.gboard.map[cur_pos[0], cur_pos[1]] = board.CHAR_DICT['S']
            for ix, step in enumerate(steplist):
                cur_pos += step
                self.gboard.map[cur_pos[0], cur_pos[1]] =board.CHAR_DICT['x']
            self.gboard.map[cur_pos[0], cur_pos[1]] = board.CHAR_DICT['K']
            # update knight position
            self.position = cur_pos



if __name__ == '__main__':
    doctest.testmod(verbose=False)
    myboard = board.Board(board.SMALL_BOARD_CHAR)
    myknight = Knight(myboard, np.array((2,3)))
    myboard.display()
    print("knight is at " + str(myknight.position))

