def find_missing_nums(nums):
    """Given an array of integers where 1 <= a[i] <= n (n=size of the array),
    some elements may appear twice and other appear once.
    Find all the elements of [1,n] inclusive that which do not appear in the
    array.
    Example:
    input = [4,3,2,7,8,2,3,1]
    output = [5,6]"""
    #I first create a set with all consecutive numbers the size of the input array
    reference = {num + 1 for num in range(len(nums))}
    #then return the difference and convert it to a list again
    return list(reference - set(nums))
