# -*- coding: utf-8 -*-
import pytest

from n_queens_problem import *


def test_under_attack_occupied_maharajah_mode_false():
    maharajah_mode = False
    existing_queens = [(3, 3), ]

    # the same
    new_queen_pos = (3, 3)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == True

    # the same row
    new_queen_pos = (3, 5)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == True

    # the same column
    new_queen_pos = (8, 3)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == True

    # left diagonal
    new_queen_pos = (4, 4)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == True

    # right diagonal
    new_queen_pos = (4, 2)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == True


def test_under_attack_free_maharajah_mode_false():
    maharajah_mode = False
    existing_queens = [(6, 5), ]

    # the other row
    new_queen_pos = (1, 1)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == False


def test_under_attack_occupied_maharajah_mode_true():
    maharajah_mode = True
    existing_queens = [(3, 3), ]

    # knight pos (+1,+2)
    new_queen_pos = (4, 5)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == True


def test_under_attack_free_maharajah_mode_true():
    maharajah_mode = True
    existing_queens = [(6, 5), ]

    # the other row
    new_queen_pos = (1, 1)
    assert under_attack(new_queen_pos[0], new_queen_pos[1], existing_queens, maharajah_mode) == False


@pytest.fixture(scope='function', params=[(1, 1),
                                          (2, 0),
                                          (3, 0),
                                          (4, 2),
                                          (5, 10),
                                          (6, 4),
                                          (7, 40),
                                          (8, 92),
                                          (9, 352),
                                          (10, 724),
                                          (11, 2680), ])
def param_test(request):
    return request.param


def test_solve_maharajah_mode_false(param_test):
    maharajah_mode = False
    (size, expected_solutions_num) = param_test
    solutions = solve(size, maharajah_mode)
    assert len(solutions) == expected_solutions_num


@pytest.fixture(scope='function', params=[(1, 1),
                                          (2, 0),
                                          (3, 0),
                                          (4, 0),
                                          (5, 0),
                                          (6, 0),
                                          (7, 0),
                                          (8, 0),
                                          (9, 0),
                                          (10, 4),
                                          (11, 44), ])
def param_test_maharajah_mode_true(request):
    return request.param


def test_solve_maharajah_mode_true(param_test_maharajah_mode_true):
    maharajah_mode = True
    (size, expected_solutions_num) = param_test_maharajah_mode_true
    solutions = solve(size, maharajah_mode)
    assert len(solutions) == expected_solutions_num
