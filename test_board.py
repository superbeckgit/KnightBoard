#!/home/mbeck/anaconda/bin/python
# -*- coding: utf-8 -*-
r"""
Test file for board class

Written by Matt Beck Sept 2015
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
import numpy as np
import unittest
import board
from dcstools.utils import capture_output

#%%
class Test_board_class(unittest.TestCase):
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
        r""" test initialization of good board layouts """
        board.Board(self.goodlayout1)
        board.Board(self.goodlayout2)
        self.assertTrue(True)

    def test_bad_board_init(self):
        r""" test initialization of bad board layouts """
        with self.assertRaises(KeyError):
            board.Board(self.badcharlayout1)
        with self.assertRaises(IndexError):
            board.Board(self.emptylayout2)

    def test_good_board_display(self):
        r""" test display of good board layouts """
        # test manual good layout
        b1 = board.Board(self.goodlayout1)
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        expected_out = """W R B S E\nK x T L ."""
        self.assertEqual(my_out, expected_out)
        # test automatic good layout
        b2 = board.Board(self.goodlayout2)
        with capture_output() as (out, _):
            b2.display()
        my_out = out.getvalue().strip()
        out.close()
        expected_out = ' '.join(board.CHAR_DICT.keys())
        self.assertEqual(my_out, expected_out)


#%% if name is main
if __name__ == '__main__':
    unittest.main(exit=False)
