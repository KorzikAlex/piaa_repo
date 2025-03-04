"""
Главный файл программы. Содержит функции для проверки времени выполнения алгоритма.

Вар. 2и. Итеративный бэктрекинг. Исследование времени выполнения от
размера квадрата.
"""
import timeit

from modules.board import Board
from modules.backtracking import backtracking_algorithm

def time_check() -> None:
    """
    Эта функция проверяет время выполнения алгоритма поиска с возвратом.
    :return:
    """
    n_sizes: list[int] = [2, 3, 4, 7, 9, 15, 17, 19]
    for n in n_sizes:
        exec_time: float = timeit.timeit(lambda: backtracking_algorithm(Board(n)), number=1)
        print(f"Время выполнения для доски размером {n}*{n}: {exec_time:.6f} секунд.")


def main() -> None:
    """
    Главная функция.
    :return:
    """
    n: int = int(input())
    result: list[list[int]] = backtracking_algorithm(Board(n))
    result: list[list[int]] = [[comp[0] + 1, comp[1] + 1, comp[2]] for comp in result]
    print(len(result))
    for square in result:
        print(*square)


if __name__ == "__main__":
    main()
    # time_check()
