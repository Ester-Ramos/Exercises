def recursive_binary(array, target):

    size = len(array)

    middle_position = (size-1)//2

    middle_element = array[middle_position]

    if middle_element == target:
        return True

    elif size <= 1:
        return False

    elif middle_element < target:
        return recursive_binary(array[middle_position+1:], target)

    else:
        return recursive_binary(array[:middle_position], target)
