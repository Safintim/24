import unittest
import task9 as t


class MyTestCase(unittest.TestCase):
    def test1(self):
        first_arr = '''4 6
                    029402
                    560202
                    029694
                    780288'''
        second_arr = '''2 2
                        02
                        94'''
        self.assertTrue(t.is_second_arr_in_first_arr(first_arr, second_arr))

    def test2(self):
        first_arr = '''3 3
                    321
                    694
                    798'''
        second_arr = '''2 2
                        69
                        98'''
        self.assertFalse(t.is_second_arr_in_first_arr(first_arr, second_arr))

    def test3(self):
        first_arr = '''15 15
            900934352126360
            119214144058652
            979486082875698
            322436531185165
            887105930987956
            232802644488782
            302771989566798
            073573207654780
            311755785362806
            909007939272309
            395094805516080
            562910805349811
            993854324744973
            768703404219199
            630625270887199'''
        second_arr = '''2 2
                        99
                        99'''
        self.assertTrue(t.is_second_arr_in_first_arr(first_arr, second_arr))

    def test4(self):
        first_arr = '''5 15
            000000000000000
            000000000000000
            000000100000000
            000000000000000
            000000000000000'''
        second_arr = '''3 5
                    00000
                    00000
                    00001'''
        self.assertTrue(t.is_second_arr_in_first_arr(first_arr, second_arr))


if __name__ == '__main__':
    unittest.main()
