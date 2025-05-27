#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Главный файл программы. Содержит функции для проверки времени выполнения алгоритма.

Вар. 2и. Итеративный бэктрекинг. Исследование времени выполнения от
размера квадрата.
"""
from timeit import timeit

from modules.board import Board
from modules.backtracking import backtracking_algorithm, silent_backtracking


def time_check() -> None:
    """
    Эта функция проверяет время выполнения алгоритма поиска с возвратом.
    :return: None
    """
    n_sizes: list[int] = list(range(2, 21))
    result_time: float = 0.0
    n: int
    for n in n_sizes:
        exec_time: float = timeit(lambda: silent_backtracking(n), number=1)
        result_time += exec_time
        print(
            f"Время выполнения для доски размером {n}*{n}:"
            f"\t{exec_time:.6f} сек.".replace(".", ",", 1)
        )
    print(f"\nОбщее время выполнения: {result_time:.6f} сек.")


def main() -> None:
    """
    Главная функция.
    :return: None
    """
    # ввод размера доски
    while True:
        try:
            n: int = int(input())
            if not 2 <= n <= 60:
                print(
                    "Ошибка: размер доски должен быть "
                    "натуральным целым числом в диапазоне от [2, 20]."
                )
                continue
            break
        except ValueError:
            print("Ошибка: введено не целое натуральное число в диапазоне от [2, 20].")

    # алгоритм бэктрекинга вернёт список квадратов (x, y, w)
    result: list[list[int]] = backtracking_algorithm(Board(n))
    # преобразуем координаты (они от 1 до N)
    result: list[list[int]] = [[comp[0] + 1, comp[1] + 1, comp[2]] for comp in result]
    print()
    # выведем кол-во квадратов
    print(len(result))
    # вывод квадратов
    for square in result:
        print(*square)


if __name__ == "__main__":
    # главная функция
    main()

    # проверка времени выполнения алгоритма в зависимости от размера квадратов
    # (раскомментировать при необходимости)
    # time_check()
