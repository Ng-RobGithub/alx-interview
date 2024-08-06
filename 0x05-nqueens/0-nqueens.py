#!/usr/bin/python3
"""N Queens Algorithm with Backtracking (Recursion inside loop)."""
import sys


class NQueen:
    """Class for solving N Queen Problem."""

    def __init__(self, n):
        """Initialize the board and results."""
        self.n = n
        self.positions = [0 for _ in range(n + 1)]
        self.results = []

    def place(self, queen_number, column):
        """Check if the queen can be placed at the given position.

        Args:
            queen_number (int): The queen number.
            column (int): The column to place the queen.

        Returns:
            bool: True if the queen can be placed, False otherwise.
        """
        for i in range(1, queen_number):
            if self.positions[i] == column or \
               abs(self.positions[i] - column) == abs(i - queen_number):
                return False
        return True

    def n_queen(self, queen_number):
        """Place queens on the board recursively.

        Args:
            queen_number (int): The starting queen number to evaluate.

        Returns:
            list: A list of solutions, each solution is a list of positions.
        """
        for column in range(1, self.n + 1):
            if self.place(queen_number, column):
                self.positions[queen_number] = column
                if queen_number == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.positions[i] - 1])
                    self.results.append(solution)
                else:
                    self.n_queen(queen_number + 1)
        return self.results


# Main
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen_solver = NQueen(N)
solutions = queen_solver.n_queen(1)

for solution in solutions:
    print(solution)
