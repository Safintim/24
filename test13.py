import unittest
import task13 as t


class MyTestCase(unittest.TestCase):
    def test_try_first_case(self):

        self.assertTrue(t.try_ascending_sort([1, 3, 2], [1, 2, 3]))
        self.assertTrue(t.try_ascending_sort([3, 2, 1], [1, 2, 3]))
        self.assertTrue(t.try_ascending_sort([1, 4, 3, 2, 5], [1, 2, 3, 4, 5]))
        self.assertTrue(t.try_ascending_sort([1, 7, 5, 3, 9], [1, 3, 5, 7, 9]))
        self.assertFalse(t.try_ascending_sort([9, 5, 3, 7, 1], [1, 3, 5, 7, 9]))
        self.assertFalse(t.try_ascending_sort([9, 5, 3, 7, 1], [1, 3, 5, 7, 9]))

    def test_try_second_case(self):
        self.assertTrue(t.try_ascending_sort([1, 3, 2], [1, 2, 3]))
        self.assertTrue(t.try_ascending_sort([3, 2, 1], [1, 2, 3]))
        self.assertTrue(t.try_ascending_sort([1, 4, 3, 2, 5], [1, 2, 3, 4, 5]))
        self.assertTrue(t.try_ascending_sort([1, 7, 5, 3, 9], [1, 3, 5, 7, 9]))
        self.assertFalse(t.try_ascending_sort([9, 5, 3, 7, 1], [1, 3, 5, 7, 9]))
        self.assertFalse(t.try_ascending_sort([9, 5, 3, 7, 1], [1, 3, 5, 7, 9]))


if __name__ == '__main__':
    unittest.main()
