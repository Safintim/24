import unittest
import task5 as t


class MyTestCase(unittest.TestCase):
    def test_tree_of_life_andrassyl1(self):
        text = '''
.+..
..+.
.+..'''
        rows = 3
        columns = 4
        age = 5

        t.tree_of_life_andrassyl(rows, columns, age, text)

    def test_tree_of_life_andrassyl2(self):
        text = '''
.......
...+...
....+..
.......
++.....
++.....
'''
        rows = 6
        columns = 7
        age = 24

        t.tree_of_life_andrassyl(rows, columns, age, text)

    def test_tree_of_life_andrassyl3(self):
        rows = 6
        columns = 7
        age = 5

        t.tree_of_life_andrassyl(rows, columns, age)


if __name__ == '__main__':
    unittest.main()
