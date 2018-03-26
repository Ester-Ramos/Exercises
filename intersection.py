def intersection(x, y):
    """Given two list x and y it finds the numbers shared in the two of them
    Example:
    x = [1,2,7,9]
    y = [2,6,7,8]
    output = [2,7]"""

    y = set(y)
    inter = []
    for num in x:
        if num in y:
            inter.append(num)
    return inter

def intersection_fast(x, y):
    """The same as before but working fully with sets"""
    return set(x).intersection(set(y))
