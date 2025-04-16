import unittest

from binary import buggy_binary


class Tests(unittest.TestCase):

    def test_empty(self):
        """Test empty array"""
        self.assertFalse(buggy_binary([], 1))

    def test_left_odd(self):
        """Test n is in left half of odd-len list"""
        self.assertTrue(buggy_binary([1, 2, 3, 4, 5], 1))

    def test_left_even(self):
        """Test n is in left half of even-len list"""
        self.assertTrue(buggy_binary([1, 2, 3, 4], 1))

    def test_right_odd(self):
        """Test n is in right half odd-len list"""
        self.assertTrue(buggy_binary([1, 2, 3, 4, 5], 5))

    def test_right_even(self):
        """Test n is in right half even-len list"""
        self.assertTrue(buggy_binary([1, 2, 3, 4], 4))

    def test_is_midpoint_odd(self):
        """Test n is in middle of odd-len list"""
        self.assertTrue(buggy_binary([1, 2, 3, 4, 5], 3))

    def test_is_midpoint_even(self):
        """Test n is in middle of even-len list"""
        self.assertTrue(buggy_binary([1, 2, 3, 4], 3))

    def test_not_in_left(self):
        """Test n not in left half of list"""
        self.assertFalse(buggy_binary([1, 2, 3, 4, 5], 0))

    def test_not_in_right(self):
        """Test n not in left half of list"""
        self.assertFalse(buggy_binary([1, 2, 3, 4, 5], 6))


if __name__ == "__main__":
    unittest.main(verbosity=2)
