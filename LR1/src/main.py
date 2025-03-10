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
    n_sizes: list[int] = list(range(2, 21)) # все размеры от 2 до 20
    result_time: int = 0
    for n in n_sizes:
        exec_time: float = timeit.timeit(lambda: backtracking_algorithm(Board(n)), number=1) # время выполнения
        result_time += exec_time
        print(f"Время выполнения для доски размером {n}*{n}: {exec_time:.6f} секунд.") # вывод времени
    print(f"Общее время выполнения: {result_time:.6f} секунд.") # вывод общего времени


def main() -> None:
    """
    Главная функция.
    :return:
    """
    # ввод размера доски
    while True:
        try:
            n: int = int(input())
            if n < 1:
                print("Ошибка: размер доски должен быть натуральным целым числом.")
                continue
            break
        except ValueError:
            print("Ошибка: введено не целое натуральное число.")

    # алгоритм бэктрекинга вернёт список квадратов (x, y, w)
    result: list[list[int]] = backtracking_algorithm(Board(n))
    # преобразуем координаты (они от 1 до N)
    result: list[list[int]] = [[comp[0] + 1, comp[1] + 1, comp[2]] for comp in result]
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
