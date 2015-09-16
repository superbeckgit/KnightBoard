#!/home/mbeck/anaconda/bin/python
# -*- coding: utf-8 -*-
r"""
Test file for knight class

Written by Matt Beck Sept 2015
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
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
        r""" make board layouts """
        # all chars manually
        self.goodlayout1 = r"""
        W R B S E
        K x T L .
        """
        # all chars automatically
        self.goodlayout2 = ' '.join(board.CHAR_DICT.keys())
        # bad char
        self.badcharlayout1 = r"""
        . Z
        . .
        """
        # no chars
        self.emptylayout2 = r""" """

    def test_good_board_inits(self):
        board.Board(self.goodlayout1)
        board.Board(self.goodlayout2)
        self.assertTrue(True)

    def test_bad_board_init(self):
        with self.assertRaises(KeyError):
            board.Board(self.badcharlayout1)
        with self.assertRaises(IndexError):
            board.Board(self.emptylayout2)

    def test_good_board_display(self):
        b1 = board.Board(self.goodlayout1)
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        expected_out = 'W R B S E\nK x T L .'
        self.assertEqual(my_out, expected_out)

if __name__ == '__main__':
    unittest.main(exit=False)
