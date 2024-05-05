#!/usr/bin/python3
"""
Script to generate and print Pascal's triangle.
"""


def generate_pascal_triangle(n):
    """
    Generate Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: Pascal's triangle as a list of lists.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)
    return triangle


def print_triangle(triangle):
    """
    Print Pascal's triangle.

    Args:
        triangle (list): Pascal's triangle as a list of lists.

    Returns:
        list: Pascal's triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
    return triangle


if __name__ == "__main__":
    print_triangle(generate_pascal_triangle(5))
