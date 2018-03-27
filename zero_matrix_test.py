import unittest
from zero_matrix import zero_matrix

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(zero_matrix([[0, 1, 2, 3], [1, 2, 3, 0], [1, 2, 3, 4], [1, 2, 3, 4]]), [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 3, 0], [0, 2, 3, 0]])
        self.assertEqual(zero_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 0, 15, 16]]), [[1, 0, 3, 4], [5, 0, 7, 8], [9, 0, 11, 12], [0, 0, 0, 0]])
        self.assertEqual(zero_matrix([[1, 2, 3, 4, 0], [0, 7, 8, 9, 10], [11, 0, 13, 0, 15], [16, 17, 0, 19, 20]]), [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])




if __name__ == "__main__":
    unittest.main()
