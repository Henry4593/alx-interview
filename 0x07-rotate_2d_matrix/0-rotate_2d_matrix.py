#!/usr/bin/python3
"""
This module provides a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): A 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in place.
    """
    # Step 1: Transpose the matrix (swap rows with columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()
