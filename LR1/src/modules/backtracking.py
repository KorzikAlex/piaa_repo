"""
This module contains the backtracking algorithm.
"""
from modules.board import Board


def is_prime(n: int) -> bool:
    """
    This function checks if a number is prime.
    :param n:
    :return:
    """
    if n < 2:
        return False
    for i in (2, n ** 0.5 + 1):
        if n % i == 0:
            return False
    return True


def backtracking_algorithm(board: Board) -> list[list[int, int, int]]:
    """
    This function implements the backtracking algorithm.
    :param board:
    :return:
    """
    # TODO: дописать алгоритм поиска с возвратом.
    if board.size % 2 == 0:
        board.place_squares_for_even_size()
    elif is_prime(board.size):
        pass
    return board.square_list
