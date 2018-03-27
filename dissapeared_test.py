import unittest
from dissapeared import find_missing_nums

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(find_missing_nums([4,3,2,7,8,2,3,1]), [5,6])
        self.assertEqual(find_missing_nums([4,3,2,7,8,2,3,1,5,6]), [9,10])
        self.assertEqual(find_missing_nums([4,3,2,7,8,1,5,6]), [])


if __name__ == "__main__":
    unittest.main()
