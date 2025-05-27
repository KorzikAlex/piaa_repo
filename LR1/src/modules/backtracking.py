#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Этот модуль содержит функции для алгоритма поиска с возвратом.
"""
from copy import deepcopy
import sys
import io

from modules.board import Board


def is_prime(n: int) -> bool:
    """
    Эта функция проверяет, является ли число простым.
    :param n:
    :return: True, если число простое, иначе False
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
    :return: Кортеж из двух делителей числа n
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return 1, n


def scale_board(board: Board, mult: int) -> Board:
    """
    Эта функция масштабирует доску.
    :param board: Исходная доска, которую нужно масштабировать
    :param mult: Множитель масштабирования
    :return: Масштабированная доска
    """
    print(f"Масштабируем доску {board.size}x{board.size} в {mult} раз")
    new_board: Board = Board(board.size * mult)
    for square in board.square_list:
        new_board.add_square(square[0] * mult, square[1] * mult, square[2] * mult)
    print(f"Новый размер доски: {new_board.size}x{new_board.size}")
    return new_board


def backtracking_fill_board(board: Board) -> Board:
    """
    Эта функция возвращает доску с заполненными квадратами.
    :param board: Исходная доска, которую нужно заполнить
    :return: Доска с заполненными квадратами или исходная доска, если заполнение невозможно
    """
    iter_queue: list[Board] = [board]
    count_steps: int = 0
    while iter_queue:
        count_steps += 1
        current_board: Board = iter_queue.pop(0)
        print(f"\nШаг {count_steps}. Текущая доска:")
        current_board.render_board()
        if current_board.is_fill():
            print(f"Найдено полное заполнение за {count_steps} шагов!")
            return current_board
        empty_x, empty_y = current_board.get_empty_cell()
        print(f"Пытаемся заполнить ячейку ({empty_x}, {empty_y})")
        for i in range(current_board.size, 0, -1):
            if current_board.check_possible_square(empty_x, empty_y, i):
                print(f"Пробуем квадрат размером {i}x{i} в позиции ({empty_x}, {empty_y})")
                new_board: Board = deepcopy(current_board)
                new_board.add_square(empty_x, empty_y, i)
                new_board.render_board()
                if new_board.is_fill():
                    print(f"Полное заполнение достигнуто на шаге {count_steps}!")
                    return new_board
                iter_queue.append(new_board)
    return board

def backtracking_algorithm(board: Board) -> list[list[int]]:
    """
    Эта функция реализует алгоритм поиска с возвратом.
    :param board: Исходная доска, которую нужно заполнить.
    :return: Список квадратов, которые были добавлены на доску.
    """
    if board.size % 2 == 0:
        print("Чётный размер - расставляем 4 квадрата")
        board.place_squares_for_even_size()
        board.render_board()
        return board.square_list
    if is_prime(board.size):
        print(f"Простой размер {board.size} - расставляем 3 квадрата")
        board.place_squares_for_prime_size()
        print("\nЗапуск поиска с возвратом для заполнения оставшихся клеток")
        board = backtracking_fill_board(board)
        board.render_board()
        return board.square_list
    small_div, big_div = get_divisors(board.size)
    print(f"Составной размер {board.size} = {small_div} * {big_div}")
    small_board: Board = Board(small_div)
    if is_prime(small_div):
        print(f"Внутренний размер {small_div} простой - расставляем 3 квадрата")
        small_board.place_squares_for_prime_size()
    small_board: Board = backtracking_fill_board(small_board)
    print(f"\nМасштабирование результата в {big_div} раз")
    board = scale_board(small_board, big_div)
    board.render_board()
    return board.square_list

def silent_backtracking(n: int) -> None:
    """
    Обертка для подавления вывода алгоритма.
    :param n: Размер доски
    :return: None
    """
    original_stdout: sys = sys.stdout
    sys.stdout = io.StringIO()  # Перенаправляем вывод в буфер
    backtracking_algorithm(Board(n))
    sys.stdout.close()
    sys.stdout = original_stdout  # Восстанавливаем вывод
