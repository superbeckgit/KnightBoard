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
    Tests knight movement functions with following scenarios:
        all valid moves
        off the board
        onto terrain
        over terrain
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
        self.small_ter = r"""
            . . . . . . . .
            . W . . . . . .
            . . R . . . . .
            . . . B . . . .
            . . . . T . . .
            . . . . . L . .
            . . . . . . . .
            """

    def test_good_knight_init(self):
        r""" initialize knight in valid location/terrain """
        b1    = board.Board(self.small_plain)
        cent  = np.array((3, 3), dtype='int')
        k1    = knight.Knight(b1,cent)
        self.assertTrue((k1.position == cent).all())
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
        r""" test valid moves in order {0, 5, 6, 3, 2, 7, 1, 4} """
        b1    = board.Board(self.small_plain)
        start = np.array((3, 3), dtype='int')
        k1    = knight.Knight(b1,start)
        # set move choice 0
        move_choice = 0
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
        #
        # set move choice 5
        move_choice = 5
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((3, 5), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in
                      """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . S x K . .
                         . . . x x . . .
                         . . . x S . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        #
        # set move choice 6
        move_choice = 6
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((2, 7), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in
                      """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . K
                         . . . S x S x x
                         . . . x x . . .
                         . . . x S . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        #
        # set move choice 3
        move_choice = 3
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((1, 5), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in
                      """. . . . . . . .
                         . . . . . K . .
                         . . . . . x x S
                         . . . S x S x x
                         . . . x x . . .
                         . . . x S . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        #
        # set move choice 2
        move_choice = 2
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((2, 3), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in
                      """. . . . . . . .
                         . . . x x S . .
                         . . . K . x x S
                         . . . S x S x x
                         . . . x x . . .
                         . . . x S . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        #
        # reset board
        b1    = board.Board(self.small_plain)
        start = np.array((3, 3), dtype='int')
        k1    = knight.Knight(b1,start)
        # set move choice 7
        move_choice = 7
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((4, 5), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in
                      """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . S x x . .
                         . . . . . K . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        #
        # set move choice 1
        move_choice = 1
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((6, 4), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in
                      """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . S x x . .
                         . . . . . S . .
                         . . . . . x . .
                         . . . . K x . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)
        #
        # set move choice 4
        move_choice = 4
        # change the board layout to reflect the move
        k1.execute_move(move_choice)
        self.assertTrue((k1.position == np.array((4, 3), dtype='int')).all())
        # confirm state of board
        with capture_output() as (out, _):
            b1.display()
        my_out = out.getvalue().strip()
        out.close()
        out_list = [ each.strip() for each in
                      """. . . . . . . .
                         . . . . . . . .
                         . . . . . . . .
                         . . . S x x . .
                         . . . K x S . .
                         . . . . x x . .
                         . . . . S x . .
                         . . . . . . . .""".split('\n')]
        expected_out = '\n'.join(out_list)
        self.assertEqual(my_out, expected_out)

    def test_move_off_board(self):
        r""" test moving off the board """
        # move off bottom of board
        b1    = board.Board(self.small_plain)
        start = np.array((6, 3), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 0
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertFalse(isvalid)
        self.assertEqual(cost, 1)

        # move off right of board
        start = np.array((3, 6), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 6
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertFalse(isvalid)
        self.assertEqual(cost, 1)

        # move off top of board
        start = np.array((1, 6), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 5
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertFalse(isvalid)
        self.assertEqual(cost, 1)

        # move off left of board
        start = np.array((1, 1), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 2
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertFalse(isvalid)
        self.assertEqual(cost, 1)

    def test_move_onto_terrain(self):
        r""" test moving onto terrain (WLBR) """
        # move onto Water (1 extra)
        b1    = board.Board(self.small_ter)
        start = np.array((0, 3), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 2
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertTrue(isvalid)
        self.assertEqual(cost, 2)

        # move onto Lava (4 extra)
        start = np.array((3, 4), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 0
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertTrue(isvalid)
        self.assertEqual(cost, 5)

        # move onto Barrier (illegal)
        start = np.array((1, 4), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 1
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertFalse(isvalid)

        # move onto Rock (illegal)
        start = np.array((1, 0), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 7
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertFalse(isvalid)


    def test_move_over_terrain(self):
        r""" test moving over terrain (WLBR) """
        # move over Water (0 extra)
        b1    = board.Board(self.small_ter)
        start = np.array((0, 1), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 1
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertTrue(isvalid)
        self.assertEqual(cost, 1)
        #
        # move over Lava (0 extra)
        start = np.array((5, 4), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 6
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertTrue(isvalid)
        self.assertEqual(cost, 1)
        #
        # move over Barrier (illegal)
        start = np.array((2, 3), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 0
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertFalse(isvalid)
        #
        # move over Rock (0 extra)
        start = np.array((2, 3), dtype='int')
        k1    = knight.Knight(b1, start)
        # set move choice
        move_choice = 2
        # determine move validity and cost
        (cost, isvalid) = k1.validate_move(move_choice)
        self.assertTrue(isvalid)
        self.assertEqual(cost, 1)


if __name__ == '__main__':
    unittest.main(exit=False)

