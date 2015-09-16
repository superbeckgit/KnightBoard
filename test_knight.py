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
        out_list = [ each.strip() for each in 
                      """. . . . . . . .
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
        out_list = [ each.strip() for each in 
                      """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . K . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        # set move choice
        move_choice = 0
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertTrue(isvalid)
        self.assertEqual(cost, 1)
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((5, 4), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in 
                      """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . S . . . .
                         . . . x . . . .
                         . . . x K . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)        
        self.assertEqual(my_out, expected_out)


           

if __name__ == '__main__':
    unittest.main(exit=False)
