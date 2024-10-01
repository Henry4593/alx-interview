"""Module to define pascal's triangle"""


def pascal_triangle(n):
    """Generates Pascal's triangle up to the specified number of rows using
       recursion.
    """
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        prev_triangle = pascal_triangle(n-1)
        last_row = prev_triangle[-1]
        new_row = [1]
        for idx in range(len(last_row)-1):
            new_row.append(last_row[idx] + last_row[idx+1])
        new_row.append(1)
        prev_triangle.append(new_row)
    return prev_triangle
