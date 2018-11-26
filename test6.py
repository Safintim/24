import unittest
import task6 as t
import time


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

    def test_time(self):
        start1 = time.time()
        t1 = self.factorial(25)
        end1 = time.time() - start1

        start2 = time.time()
        for i in t.factorial(25):
            t2 = i
        end2 = time.time() - start2
        self.assertEqual(t1, t2)
        print(end2 / end1)
        print(end1)
        print(end2)


if __name__ == '__main__':
    unittest.main()
