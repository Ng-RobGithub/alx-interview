#!/usr/bin/python3
"""
N Queens Puzzle Solver using Backtracking
"""
import sys


class NQueenSolver:
    """Class to solve the N Queens problem using backtracking."""

    def __init__(self, n):
        """Initialize the board size and solution storage."""
        self.n = n
        self.positions = [0] * (n + 1)
        self.solutions = []

    def can_place(self, current_queen, column):
        """
        Check if the current queen can be placed in the given column.
        Ensures no queens are attacking each other.
        """
        for previous_queen in range(1, current_queen):
            if self.positions[previous_queen] == column or \
               abs(self.positions[previous_queen] - column) == abs(
                   previous_queen - current_queen):
                return False
        return True

    def solve(self, current_queen=1):
        """
        Recursively attempt to place queens on the board.
        Args:
            current_queen: The queen to be placed.
        """
        for column in range(1, self.n + 1):
            if self.can_place(current_queen, column):
                self.positions[current_queen] = column
                if current_queen == self.n:
                    # A solution is found
                    self.add_solution()
                else:
                    # Try to place next queen
                    self.solve(current_queen + 1)
        return self.solutions

    def add_solution(self):
        """Store the current board configuration as a solution."""
        solution = []
        for queen in range(1, self.n + 1):
            solution.append([queen - 1, self.positions[queen] - 1])
        self.solutions.append(solution)


def main():
    """Main function to handle input and solve the N Queens problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solver = NQueenSolver(n)
    solutions = solver.solve()

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
