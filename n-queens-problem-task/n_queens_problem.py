# -*- coding: utf-8 -*-
import argparse

import sys

try:
    xrange
except NameError:
    xrange = range

KNIGHT_MOVEMENTS = (
    # Top-right movements.
    (+2, +1), (+1, +2),
    # Top-left movements.
    (-2, +1), (-1, +2),
    # Bottom-right movements.
    (+2, -1), (+1, -2),
    # Bottom-left movements.
    (-2, -1), (-1, -2),
)


def under_attack(row, column, existing_queens, maharajah_mode):
    if not len(existing_queens): return False
    for queen in existing_queens:
        if not len(queen):
            continue
        r, c = queen
        if r == row: return True  # Check row
        if c == column: return True  # Check column
        if (column - c) == (row - r): return True  # Check left diagonal
        if (column - c) == -(row - r): return True  # Check right diagonal
        if maharajah_mode:
            for step in KNIGHT_MOVEMENTS:  # Check knights movements
                if (r + step[0] == row) and (c + step[1] == column):
                    return True
    return False


def check(solutions, row, n, maharajah_mode):
    new_solutions = []
    for column in range(n):
        if not solutions or not len(solutions):
            new_solutions.append([] + [(row, column)])
        else:
            for solution in solutions:
                if not under_attack(row, column, solution, maharajah_mode):
                    new_solutions.append(solution + [(row, column)])
    return new_solutions


def solve(n, maharajah_mode):
    solutions = []
    for row in range(n):
        solutions = check(solutions, row, n, maharajah_mode)
    if solutions and len(solutions[0]) == n:
        return solutions
    return []


def show(solution):
    size = len(solution)
    for row in xrange(size):
        row_out = ""
        for column in xrange(size):
            if (row, column) in solution:
                row_out += '|Q'
            else:
                row_out += '| '
        row_out += '|'
        print(row_out)


def parse_args(args):
    parser = argparse.ArgumentParser(description="All possible solution of the n-Queen's problem")
    parser.add_argument('n', type=int, default=1, help='Board size')
    parser.add_argument('-r', '--render', action='store_true', help='print last solution')
    parser.add_argument('-m', '--maharajah_mode', action='store_true', help='Maharajah mode')
    if not args:
        parser.print_help()
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    solutions = solve(args.n, args.maharajah_mode)
    print('Number of solutions: ' + str(len(solutions)))
    if solutions and args.render:
        print('Last solution: ')
        show(solutions[-1])
