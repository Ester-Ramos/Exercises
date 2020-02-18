
def binary_search(array, target):

    left_element = 0
    right_element = len(array) - 1

    while left_element <= right_element:

        middle_element = (left_element + right_element) // 2

        if array[middle_element] == target:
            return True

        elif array[middle_element] > target:
            right_element = middle_element - 1

        else:
            left_element = middle_element + 1

    return False
