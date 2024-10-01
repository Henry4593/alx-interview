"""Module to define pascal's triangle"""


def pascal_triangle(n):
    """implements pascal's triangle using recursion"""
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        current_row = [1]
        prev_row = pascal_triangle(n-1)
        for idx in range(len(prev_row)-1):
            current_row.append(prev_row[idx] + prev_row[idx+1])
        current_row += [1]
    return current_row
