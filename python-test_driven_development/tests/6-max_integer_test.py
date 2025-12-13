#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list"""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_beginning(self):
        """Test a list with max at the beginning"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        """Test a list with max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_one_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test an empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_negatives(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_int_float(self):
        """Test a list with mixed int and float"""
        self.assertEqual(max_integer([1, 2.5, 3, 0.5]), 3)

    def test_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_list_of_lists(self):
        """Test a list of lists (compares by first element)"""
        self.assertEqual(max_integer([[1, 2], [3, 4], [0, 5]]), [3, 4])


if __name__ == "__main__":
    unittest.main()
