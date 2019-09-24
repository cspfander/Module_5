import unittest
from input_loops import average_input_scores


class MyTestCase(unittest.TestCase):
    def test_average(self):
        self.assertEqual(85, average_input_scores.average([85, 90, 80]))


if __name__ == '__main__':
    unittest.main()
