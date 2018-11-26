import unittest
import task6 as t


class MyTestCase(unittest.TestCase):
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)

    def test_summation(self):
        for i in range(10**4 + 1):
            s = t.summation(str(10**8), str(i))
            self.assertEqual(int(s), 10**8 + i)

    def test_factorial(self):
        task6_fact = t.factorial(25)
        for i in range(1, 26):
            self.assertEqual(next(task6_fact), self.factorial(i))


if __name__ == '__main__':
    unittest.main()
