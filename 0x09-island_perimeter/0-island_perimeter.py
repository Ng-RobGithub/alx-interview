#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A list of lists of integers representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for the current land cell
                perimeter += 4

                # Check left neighbor
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

                # Check upper neighbor
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

    return perimeter
