#!/usr/bin/python3
"""
N Queens Problem Solver using Backtracking
"""

import sys


class NQueen:
    """Class for solving N Queen Problem"""

    def __init__(self, n):
        """Initialize the board and solution list"""
        self.n = n
        self.board = [0] * (n + 1)
        self.solutions = []

    def can_place(self, row, col):
        """
        Check if a queen can be placed on the board at (row, col)
        """
        for i in range(1, row):
            if self.board[i] == col or \
               abs(self.board[i] - col) == abs(i - row):
                return False
        return True

    def solve(self, row):
        """
        Recursively try to place queens on the board
        """
        for col in range(1, self.n + 1):
            if self.can_place(row, col):
                self.board[row] = col
                if row == self.n:
                    self.add_solution()
                else:
                    self.solve(row + 1)
        return self.solutions

    def add_solution(self):
        """
        Add the current board configuration to the list of solutions
        """
        solution = []
        for i in range(1, self.n + 1):
            solution.append([i - 1, self.board[i] - 1])
        self.solutions.append(solution)


def main():
    """
    Main function to handle input and start solving the N Queens problem
    """
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

    queen = NQueen(n)
    solutions = queen.solve(1)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
