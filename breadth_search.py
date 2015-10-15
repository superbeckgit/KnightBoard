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
. . . . . L . .
. . . . . . . E
"""

start = np.array((18, 23), dtype='int')
goal  = np.array((20, 29), dtype='int')

b1 = board.Board(board.LARGE_BOARD_CHAR)
k1 = knight.Knight(b1, start)
num_moves = len(k1.valid_moves)

def expand_path(pathlist, num_moves):
    newpathlist = []
    for path in pathlist:
        if not (path['dest'] == goal).all():
            for move in range(num_moves):
                newpath = copy.deepcopy(path)
                newpath['moves'].append(move)
                newpathlist.append(newpath)
        else:
            newpathlist.append(path)
    return newpathlist

def trim_invalid_seq(pathlist):
    for ix, path in enumerate(pathlist):
        (path['cost'], path['valid'], path['dest']) = k1.validate_sequence(path['moves'])
        if not path['valid']:
            pass
            # print('bad move sequence = ' + str(path['moves']) + ' cost = ' + str(path['cost']))
    newpathlist = [path for path in pathlist if path['valid']==True]
    return newpathlist

def trim_inefficient(pathlist):
    # build updated dictionary of best cost per destination
    dest_cost = {}
    for path in pathlist:
        thiskey = str(path['dest'])
        # get cost for this destination
        cost = dest_cost.get(thiskey)
        if cost == None or (cost > path['cost']):
            # no cost known or this path has lower cost than stored
            # store this cost as best for this destination
            dest_cost[thiskey] = path['cost']
        elif cost >= path['cost']:
            # this destination has already been reached with same or lower cost
            path['valid'] = False
    # cull list for only shortest paths to destination
    newpathlist = [path for path in pathlist if path['cost'] == dest_cost[str(path['dest'])]
                                                and path['valid'] == True]
    return newpathlist

def check4winners(pathlist,goal):
    winners = [path for path in pathlist if (path['dest'] == goal).all()]
    return winners

# build initial pathlist
path = {}
path['moves'] = []
path['cost'] = 0
path['dest'] = start

pathlist = [path]
#trim_invalid_seq(path)
k1.gboard.display()
for iter in range(30):
    pathlist = expand_path(pathlist, num_moves)
    pathlist = trim_invalid_seq(pathlist)
    pathlist = trim_inefficient(pathlist)
    winners  = check4winners(pathlist, goal)
    if len(winners) > 0 :
        print('Winning path found at ' + str(iter+1) + ' moves:')
        print(winners[0])
        for move in winners[0]['moves']:
            k1.execute_move(move)
        k1.gboard.display()
        break