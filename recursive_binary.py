def recursive_binary(array, target):

    size = len(array)
    if size == 0:
        return False

    middle_position = (size-1)//2

    middle_element = array[middle_position]

    if middle_element == target:
        return True

    elif size == 1:
        return False

    elif middle_element < target:
        array = array[middle_position+1:]
        return recursive_binary(array, target)

    else:
        array = array[:middle_position]
        return recursive_binary(array, target)
