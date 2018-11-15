import unittest
import task2 as t


class MyTestCase(unittest.TestCase):
    def test_get_history_successes(self):
        top_list1 = [14000000, 13500000, 13500000,
                     11000000, 9000000, 9000000,
                     9000000]
        successes_data_team1 = [100000, 900000, 8000000,
                                2000000, 2700000, 100000]
        result1 = [5, 5, 4, 3, 2, 2]

        self.assertEqual(result1,t.get_history_successes(top_list1,
                                                         successes_data_team1))

        top_list2 = [100, 100, 99, 99, 99, 95, 95, 90, 90, 1, 1, 1]
        successes_data_team2 = [0, 1, 89, 4, 5, 1, 1, 1]
        result2 = [6, 5, 4, 4, 2, 1, 1, 1]

        self.assertEqual(result2, t.get_history_successes(top_list2,
                                                          successes_data_team2))

        top_list3 = [10, 9, 9, 9, 8, 7, 7, 7, 6, 5, 4, 3, 2, 2, 1]
        successes_data_team3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        result3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1]

        self.assertEqual(result3, t.get_history_successes(top_list3,
                                                          successes_data_team3))


if __name__ == '__main__':
    unittest.main()
