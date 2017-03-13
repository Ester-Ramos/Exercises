
import math

def binary_search(list, target):

    left_element = 0
    right_element = len(list) - 1

    while left_element <= right_element:

        middle_element = (left_element + right_element) // 2

        if list[middle_element] == target:
            return True

        elif list[middle_element] > target:
            right_element = middle_element - 1

        else:
            left_element = middle_element + 1

    return False

