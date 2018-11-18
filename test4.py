import unittest
import task4 as t


class MyTestCase(unittest.TestCase):
    def test_get_magic_word_from_string(self):
        test1 = 'ая'
        test2 = 'fff'
        test3 = 'нклм'
        test4 = 'вибк'
        test5 = 'вкиб'

        result1 = 'яа'
        result2 = None
        result3 = 'нкмл'
        result4 = 'викб'
        result5 = 'ибвк'

        self.assertEqual(result1, t.get_magic_word_from_string(test1))
        self.assertEqual(result2, t.get_magic_word_from_string(test2))
        self.assertEqual(result3, t.get_magic_word_from_string(test3))
        self.assertEqual(result4, t.get_magic_word_from_string(test4))
        self.assertEqual(result5, t.get_magic_word_from_string(test5))


if __name__ == '__main__':
    unittest.main()
