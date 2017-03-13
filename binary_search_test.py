import unittest
from binary_search import binary_search

class MyTest(unittest.TestCase):
    def test(self):
        self.assertTrue(binary_search([1,2,3,4,5], 4))
        self.assertFalse(binary_search([1,2,3,4,5], 0))
        self.assertTrue(binary_search([1,2,6,9,43], 2))
        self.assertTrue(binary_search([1,2,6,6,9,43], 6))
        self.assertFalse(binary_search([1,2,3,4,5], 6))
        self.assertTrue(binary_search([-2,-1,3,4,5], 5))
        self.assertTrue(binary_search([-56,-43,-20,-6,-2], -43))
        self.assertFalse(binary_search([-56,-43,-20,-6,-2], -42))
        self.assertFalse(binary_search([1,2,3,4,5], 1.5))

if __name__ == "__main__":
    unittest.main()

