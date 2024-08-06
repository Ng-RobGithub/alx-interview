#!/usr/bin/python3
"""N QUEENS ALGORITHM WITH BACKTRACKING (RECURSION INSIDE LOOP)"""

import sys


class NQueen:
    """Class for solving N Queen Problem"""

    def __init__(self, n):
        """Initialize global variables"""
        self.n = n
        self.board = [0 for _ in range(n + 1)]
        self.solutions = []

    def is_safe(self, k, i):
        """Checks if k Queen can be placed in i column (True)
        or if there are attacking queens in row or diagonal (False)"""

        # Check from 1 to k - 1 (Up to the previous queen)
        for j in range(1, k):
            # There is already a queen in the same column
            # or a queen in the same diagonal
            if self.board[j] == i or \
               abs(self.board[j] - i) == abs(j - k):
                return False
        return True

    def solve_n_queens(self, k):
        """Tries to place every queen on the board
        Args:
        k: starting queen from which to evaluate (should be 1)
        """
        for i in range(1, self.n + 1):
            if self.is_safe(k, i):
                # Queen can be placed in i column
                self.board[k] = i
                if k == self.n:
                    # Placed all N Queens (A solution was found)
                    solution = []
                    for idx in range(1, self.n + 1):
                        solution.append([idx - 1, self.board[idx] - 1])
                    self.solutions.append(solution)
                else:
                    # Need to place more Queens
                    self.solve_n_queens(k + 1)
        return self.solutions


# Main

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen_solver = NQueen(N)
results = queen_solver.solve_n_queens(1)

for solution in results:
    print(solution)
