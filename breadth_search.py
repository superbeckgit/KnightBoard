#!/home/mbeck/anaconda/bin/python
# -*- coding: utf-8 -*-
r"""
Breadth first search :
    finds shortest path from start to end
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
import knight


#%% GLOBALS
SMALL_BOARD_CHAR = r"""
S . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . E
"""

start = np.array((0, 0), dtype='int')
goal  = np.array((7, 7), dtype='int')

b1 = board.Board(SMALL_BOARD_CHAR)
k1 = knight.Knight(b1, start)
num_moves = len(k1.valid_moves)

def expand_path(path, num_moves):
    newpaths = []
    for ix, each in enumerate(path):
        for move in range(num_moves):
            subpath = copy.deepcopy(each)
            subpath.append(move)
            newpaths.append(subpath)
    return newpaths

def trim_invalid_seq(path):
    to_remove = []
    for ix, each in enumerate(path):
        (cost, valid) = k1.validate_sequence(each)
        if not valid:
            print('bad move sequence = ' + str(each) + ' cost = ' + str(cost))
            to_remove.append(ix)
    to_remove.reverse()
    for ix in to_remove:
        path.pop(ix)

path = [[move] for move in range(num_moves)]
trim_invalid_seq(path)
k1.gboard.display()
for iter in range(2):
    k1.gboard.display()
    path = expand_path(path, num_moves)
    trim_invalid_seq(path)
