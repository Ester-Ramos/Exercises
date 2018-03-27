from itertools import product

def zero_matrix(input_matrix):
    """If an element in a nxm matrix is 0 the whole row and column is set to 0.
    I first identify the zeroes, and then use those indexes to change the whole
    matrix"""

    positions = []
    for i, row in enumerate(input_matrix):
        if 0 not in row:
            continue
        positions.append((i, row.index(0)))

    d_x = len(input_matrix)
    d_y = len(input_matrix[0])
    for column, row in positions:
        for column_matrix, row_matrix in product(range(d_x), range(d_y)):
            input_matrix[column][row_matrix] = 0
            input_matrix[column_matrix][row] = 0

    return input_matrix
