import unittest
import task1 as t


class MyTestCase(unittest.TestCase):
    def test_generate_and_converter(self):
        for _ in range(100):
            random_array = t.generate_random_array(127)
            actual_array = t.converter_array_to_start_impulse(random_array)
            self.assertEqual(actual_array[len(actual_array) // 2],
                             max(random_array))
            self.assertEqual(actual_array[0], min(random_array))
            self.assertTrue(actual_array[len(actual_array) // 2 - 1] < actual_array[-2])
            self.assertTrue(actual_array[-2] < actual_array[-3])


if __name__ == '__main__':
    unittest.main()
