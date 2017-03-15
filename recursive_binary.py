def recursive_binary(list, target):

    size = len(list)
    if size == 0:
        return False

    middle_position = (size-1)//2

    middle_element = list[middle_position]

    if middle_element == target:
        return True

    elif len(list) == 1:
        return False

    elif middle_element < target:
        list = list[middle_position+1:]
        return recursive_binary(list, target)

    else:
        list = list[:middle_position]
        return recursive_binary(list, target)
