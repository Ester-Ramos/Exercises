import unittest
from move_zeroes import move_zeroes

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(move_zeroes([4, 1, 0, 3, 0]), [[4, 1, 3, 0, 0])



if __name__ == "__main__":
    unittest.main()
