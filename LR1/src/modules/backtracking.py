"""
Этот модуль содержит функции для алгоритма поиска с возвратом.
"""
from copy import deepcopy

from modules.board import Board


def is_prime(n: int) -> bool:
    """
    Эта функция проверяет, является ли число простым.
    :param n:
    :return:
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_divisors(n: int) -> tuple[int, int]:
    """
    Эта функция возвращает делители числа.
    :param n:
    :return:
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return 1, n


def scale_board(board: Board, mult: int) -> Board:
    """
    Эта функция масштабирует доску.
    :param board:
    :param mult:
    :return:
    """
    new_board: Board = Board(board.size * mult)
    for square in board.square_list:
        new_board.add_square(square[0] * mult, square[1] * mult, square[2] * mult)
    return new_board


def backtracking_fill_board(board: Board) -> Board:
    """
    Эта функция возвращает доску с заполненными квадратами.
    :param board:
    :return:
    """
    iter_queue: list[Board] = [board]
    while iter_queue:
        current_board: Board = iter_queue.pop(0)
        if current_board.is_fill():
            return current_board
        empty_x, empty_y = current_board.get_empty_cell()
        for i in range(current_board.size, 0, -1):
            if current_board.check_possible_square(empty_x, empty_y, i):
                new_board: Board = deepcopy(current_board)
                new_board.add_square(empty_x, empty_y, i)
                if new_board.is_fill():
                    return new_board
                iter_queue.append(new_board)
    return board

def backtracking_algorithm(board: Board) -> list[list[int]]:
    """
    Эта функция реализует алгоритм поиска с возвратом.
    :param board:
    :return:
    """
    if board.size % 2 == 0:
        board.place_squares_for_even_size()
        board.render_board()
        return board.square_list
    if is_prime(board.size):
        board.place_squares_for_prime_size()
        board = backtracking_fill_board(board)
        board.render_board()
        return board.square_list
    small_div, big_div = get_divisors(board.size)
    small_board: Board = Board(small_div)
    if is_prime(small_div):
        small_board.place_squares_for_prime_size()
    small_board: Board = backtracking_fill_board(small_board)
    board = scale_board(small_board, big_div)
    board.render_board()
    return board.square_list
