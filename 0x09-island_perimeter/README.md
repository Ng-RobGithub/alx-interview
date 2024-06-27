# Island Perimeter Project

## Description

This project contains a function `island_perimeter` that calculates the perimeter of an island described in a grid. The grid is a list of lists of integers where `0` represents water and `1` represents land. Each cell is square with a side length of 1. Cells are connected horizontally or vertically (not diagonally). The grid is rectangular, and the island is completely surrounded by water. There is only one island in the grid, and it does not have lakes (water inside that isn't connected to the water surrounding the island).

## Requirements

- The script is compatible with Python 3.4.3 on Ubuntu 20.04 LTS.
- The code adheres to PEP 8 style guidelines.
- No external modules are imported.
- The script is executable.

## Function

### island_perimeter

```python
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A list of lists of integers representing the grid.

    Returns:
        int: The perimeter of the island.
    """
