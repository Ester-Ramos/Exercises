def move_zeroes(nums):
    """given an array move all the zeroes to the end while maintaining the
    relative order of the non-zero elements
    Example:
    nums = [0,1,0,3,12]
    output = [1,3,12,0,0]
    """
    #I create a counter of zeroes and then add it at the end of a new list
    zeros = 0
    new_nums = []
    for num in nums:
        if num == 0:
            zeros += 1
        else:
            new_nums.append(num)

    return new_nums + [0] * zeros

def move_zeroes_in_place(nums):
    """another approach modifying the list given witout taking anymore memory"""
    #I swap each number with themselves until there's a zero, then I swap it with the next number
    current = 0
    for i, n in enumerate(nums):
        nums[current], nums[i] = nums[i], nums[current]
        current += n != 0

    return nums
