# *- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 8 Точный метод: динамическое программирование (не МВиГ), итеративная
реализация.
Приближённый алгоритм: АЛШ-2.
Требование перед сдачей: прохождение кода в задании 3.1 на Stepik.
Замечание к варианту 8 АЛШ-2 начинать со стартовой вершины.
"""
from modules.tsp import fill_dp, calc_best_path, restore_path


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    n: int = int(input())
    graph_mx: list[list[int]] = [[int(i) for i in input().split()] for _ in range(n)]

    dp: list[list[int | float]]
    parent: list[list[int]]
    dp, parent = fill_dp(n, graph_mx)

    min_total: int
    best_u: int
    min_total, best_u = calc_best_path(n, dp, graph_mx)

    if min_total == float("inf"):
        print("no path")
    else:
        print(min_total)
        print(*restore_path(n, parent, best_u))


if __name__ == '__main__':
    main()
