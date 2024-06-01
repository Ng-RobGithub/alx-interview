#!/usr/bin/python3
""" N queens """

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_n_queens_util(board, row, n):
    """
    Utilizes backtracking to solve the N Queens problem
    """
    if row == n:
        # All queens are placed successfully
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens_util(board, row + 1, n):
                return True
            # Backtrack
            board[row] = -1

    return False


def solve_n_queens(n):
    """
    Solves the N Queens problem and prints the solution
    """
    board = [-1] * n
    if solve_n_queens_util(board, 0, n):
        # Print the solution
        print_solution(board)
    else:
        print("No solution exists")


def print_solution(board):
    """
    Print the board
    """
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 n_queens.py N")
        return
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        return
    solve_n_queens(n)


if __name__ == "__main__":
    main()
