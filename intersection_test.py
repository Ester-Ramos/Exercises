import unittest
from intersection import intersection, intersection_fast

class MyTest(unittest.TestCase):
    def test(self):
        self.assertTrue(intersection([1,2,3,4,5], [0,2,4], [2,4]))
        self.assertFalse(intersection([1,2,3,4,5], [0,2,4], [0,3]))
        

if __name__ == "__main__":
    unittest.main()
