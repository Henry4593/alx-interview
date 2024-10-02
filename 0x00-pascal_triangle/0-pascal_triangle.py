#!/usr/bin/python3
"""Module to define pascal's triangle"""


def pascal_triangle(n):
    """
    Generate the first n rows of the Pascal's triangle.

    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list: A list of lists representing the Pascal's triangle.
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for row_num in range(n):
        row = [1] * (row_num + 1)
        row[1:-1] = [triangle[row_num - 1][j - 1] +
                     triangle[row_num - 1][j] for j in range(1, row_num)]
        triangle.append(row)
    return triangle
