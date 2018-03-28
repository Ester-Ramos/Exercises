import unittest
from stocks import max_profit_redux

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(max_profit_redux([7,6,4,3,1]), 0)
        self.assertEqual(max_profit_redux([]), 0)
        self.assertEqual(max_profit_redux(None), 0)
        self.assertEqual(max_profit_redux([7,1,5,3,6,4]), 5)
        self.assertEqual(max_profit_redux([2,6,1,4]), 4)



if __name__ == "__main__":
    unittest.main()
