
import math
import unittest

def binary_search(list, target):

    left_element = 0
    right_element = len(list) - 1

    while left_element <= right_element:

        middle_element = math.floor((left_element + right_element) // 2)

        if list[middle_element] == target:
            print('Found')
            return True

        elif list[middle_element] > target:
            right_element = middle_element - 1

        elif list[middle_element] < target:
            left_element = middle_element + 1

    print('Not found')
    return False

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
