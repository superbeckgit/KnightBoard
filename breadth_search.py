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
. . . . . . W .
. . . . . . . .
. . . . . . . E
"""

start = np.array((0, 0), dtype='int')
goal  = np.array((7, 7), dtype='int')

b1 = board.Board(SMALL_BOARD_CHAR)
k1 = knight.Knight(b1, start)
num_moves = len(k1.valid_moves)

def expand_path(pathlist, num_moves):
    newpathlist = []
    for ix, path in enumerate(pathlist):
        for move in range(num_moves):
            newpath = copy.deepcopy(path)
            newpath['moves'].append(move)
            newpathlist.append(newpath)
    return newpathlist

def trim_invalid_seq(pathlist):
    for ix, path in enumerate(pathlist):
        (path['cost'], path['valid'], path['dest']) = k1.validate_sequence(path['moves'])
        if not path['valid']:
            pass
            # print('bad move sequence = ' + str(path['moves']) + ' cost = ' + str(path['cost']))
    newpathlist = [path for path in pathlist if path['valid']==True]
    return newpathlist

def check4winners(pathlist,goal):
    winners = [path for path in pathlist if (path['dest'] == goal).all()]
    for each in winners:
        print(str(each['moves']) + ' ' + str(each['cost']))

# build initial pathlist
path = {}
path['moves'] = []
path['cost'] = 0
path['dest'] = start

pathlist = [path]
#trim_invalid_seq(path)
k1.gboard.display()
for iter in range(6):
    pathlist = expand_path(pathlist, num_moves)
    pathlist = trim_invalid_seq(pathlist)
    # trim for repeated destinations (keep one with lowest cost)
    check4winners(pathlist, goal)