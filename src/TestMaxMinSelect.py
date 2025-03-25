import unittest
from main import maxmin_select


class TestMaxMinSelect(unittest.TestCase):
    def test_single_element(self):
        arr = [5]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (5, 5))

    def test_two_elements(self):
        arr = [2, 8]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (2, 8))

    def test_multiple_elements(self):
        arr = [3, 1, 5, 2, 9, 8, 6]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (1, 9))

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (1, 5))

    def test_reverse_sorted_array(self):
        arr = [9, 7, 5, 3, 1]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (1, 9))

    def test_large_numbers(self):
        arr = [1000, 2000, 3000, 4000, 5000]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (1000, 5000))

    def test_negative_numbers(self):
        arr = [-10, -20, -5, -1, -30]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (-30, -1))

    def test_mixed_numbers(self):
        arr = [-5, 0, 5, -10, 10]
        self.assertEqual(maxmin_select(arr, 0, len(arr) - 1), (-10, 10))

if __name__ == "__main__":
    unittest.main()
