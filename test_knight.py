#!/home/mbeck/anaconda/bin/python
# -*- coding: utf-8 -*-
r"""
Test file for knight class

Written by Matt Beck Sept 2015
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import copy
import numpy as np
import unittest
import board
import knight
from dcstools import capture_output

#%%
class Test_knight_class(unittest.TestCase):
    r"""
    Tests validate_move function with following inputs:
        all valid moves [TBD]
        null move
        off the board
        illegal small move
        illegal big move
    """
    def setUp(self):
        r""" make board layout """
        self.small_plain =  r"""
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            . . . . . . . .
            """

    def test_good_knight_init(self):
        r""" initialize knight in valid location/terrain """
        b1    = board.Board(self.small_plain)
        cent  = np.array((3, 3), dtype='int')
        k1    = knight.Knight(b1,cent)
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . K . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)        


    def test_valid_moves(self):
        b1    = board.Board(self.small_plain)
        cent  = np.array((3, 3), dtype='int')
        k1    = knight.Knight(b1,cent)
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . K . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        move  = k1.valid_moves[0]
        # initialize move validity and cost
        isvalid = True
        cost    = 0
        test_pos = copy.deepcopy(k1.position)
        for ix, step in enumerate(move):
            test_pos += step
            # get step validity and penalty
            (step_v, step_p) = b1.validate_position(step)
            # combine step validity and move validity
            isValid = isvalid & step_v
            # add step penalty to move cost
            cost += step_p
        # add standard move cost
        cost += 1
        self.assertTrue(isvalid)
        self.assertEqual(cost, 1)
        self.assertTrue((test_pos == np.array((5, 4), dtype='int')).all())
        # change the board layout to reflect the move
        cur_pos = copy.deepcopy(k1.position)
        b1.map[cur_pos[0], cur_pos[1]] = board.CHAR_DICT['S']
        for ix, step in enumerate(move):
            cur_pos += step
            b1.map[cur_pos[0], cur_pos[1]] =board.CHAR_DICT['x']
        # update knight position
        k1.position = cur_pos
        b1.map[cur_pos[0], cur_pos[1]] = board.CHAR_DICT['K']
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        expected_out = """. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . S . . . .
. . . x . . . .
. . . x K . . .
. . . . . . . .
. . . . . . . ."""
        self.assertEqual(my_out, expected_out)

           

if __name__ == '__main__':
    unittest.main(exit=False)
