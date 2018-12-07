import unittest
import task12 as l


class MyTestCase(unittest.TestCase):

    def test_get_repeating_element(self):
        self.assertEqual(l.is_valid('xyz'), True)
        self.assertEqual(l.is_valid('xyzaa'), True)
        self.assertEqual(l.is_valid('xxyyzzz'), True)
        self.assertEqual(l.is_valid('xxyyz'), True)
        self.assertEqual(l.is_valid('xyzzz'), False)
        self.assertEqual(l.is_valid('xxyyza'), False)
        self.assertEqual(l.is_valid('xxyyzabc'), False)


if __name__ == '__main__':
    unittest.main()
