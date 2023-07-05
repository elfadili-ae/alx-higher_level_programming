#!/usr/bin/python3
"""The N queens Challenge"""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

num = int(sys.argv[1])
if num < 4:
    print("N must be at least 4")
    sys.exit(1)


def solve():
    """solve by backtracking"""
    solutions = []
    state = []
    search(state, solutions)
    displaySolution(solutions)


def is_valid_state(state):
    """Check if it's a valid solution"""
    return len(state) == num


def get_candidates(state):
    """get candidates"""
    if not state:
        return range(num)

    position = len(state)
    candidates = set(range(num))

    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions):
    """search for solutions"""
    if is_valid_state(state):
        solutions.append(state.copy())
        return

    for candidate in get_candidates(state):
        state.append(candidate)
        search(state, solutions)
        state.remove(candidate)


def displaySolution(solutions):
    """display the solution"""
    for row in solutions:
        for i in range(len(row)):
            row[i] = [i, row[i]]
    for row in solutions:
        print(row)


solve()
