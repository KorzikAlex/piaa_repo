#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 8 Точный метод: динамическое программирование (не МВиГ), итеративная
реализация.
Приближённый алгоритм: АЛШ-2.
Требование перед сдачей: прохождение кода в задании 3.1 на Stepik.
Замечание к варианту 8 АЛШ-2 начинать со стартовой вершины.
"""
from modules.tsp import fill_dp, calc_best_path, restore_path
from modules.loader import load_mx, write_mx, generate_mx
from modules.parser import get_args

INF: float = float("inf")


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    args = get_args()

    if args.generate:
        file_name: str = args.output
        n: int = args.count
        if not 5 <= args.count <= 15:
            print("Значение аргумента должно быть в диапазоне [5, 15].")
            return
        graph_mx: list[list[int]] = generate_mx(n, args.symmetric)
        if args.output:
            file_name = args.output
        write_mx(file_name, graph_mx)
        print(f"Матрица {n}×{n}"
                f"{' (симметричная)' if args.symmetric else ''} "
                f"сохранена в файл '{file_name}'")
        return

    if args.input:
        try:
            n, graph_mx = load_mx(args.input)
        except FileNotFoundError:
            print(f"Файл '{args.input}' не найден.")
            return
        except ValueError as e:
            print("Неверный формат файла.")
            return
    else:
        n: int = int(input())
        graph_mx: list[list[int]] = [[int(i) for i in input().split()] for _ in range(n)]

    if args.method == "exact":
        dp: list[list[int | float]]
        parent: list[list[int]]
        dp, parent = fill_dp(n, graph_mx)

        min_total: int
        best_u: int
        min_total, best_u = calc_best_path(n, dp, graph_mx)

        if min_total == INF:
            print("no path")
        else:
            print(min_total)
            print(*restore_path(n, parent, best_u))
    if args.method == "approx":
        return


if __name__ == '__main__':
    main()
