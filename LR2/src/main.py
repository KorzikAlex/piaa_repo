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
import argparse

from modules.tsp import fill_dp, calc_best_path, restore_path
from modules.loader import load_mx, write_mx, generate_mx

INF: float = float("inf")

def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=(
        "Решение задачи коммивояжёра двумя методами:\n"
        "    1) Точный (ДП, рекурсивно, старт из 0)\n"
        "    2) Приближённый (АЛШ-2, вариант 8)\n"
        "Кроме того, можно сгенерировать матрицу (произвольную или симметричную),\n"
        "сохранить её в файл и затем читать из файла."),
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-i", "--input", type=str, dest="input",
                        help="Имя файла с матрицей (если не указан, читаем из stdin)")
    parser.add_argument("-o", "--output", type=str, default="output.txt", dest="output",
                        help="Имя файла, в который сохраняем матрицу")
    parser.add_argument("-g", "--generate", action="store_true", dest="generate",
                        help="Сгенерировать новую матрицу весов")
    parser.add_argument("-c", "--count", type=int, default=10, dest="count",
                        help="Количество городов (5 ≤ n ≤ 15)")
    parser.add_argument("-s", "--symmetric", action="store_true", dest="symmetric",
                        help="Сгенерировать симметричную матрицу")
    parser.add_argument("--max-weight", type=int, default=100, dest="max_weight",
                        help="Максимальный вес ребра (по умолчанию 100)")
    parser.add_argument("--method", choices=["exact", "approx"], default="exact",
                        help="Метод решения: exact — точный (DP), approx — приближённый (АЛШ-1)")
    args = parser.parse_args()

    if args.generate:
        graph_mx: list[list[int]] = generate_mx(args.count, args.symmetric)
        write_mx(args.output, graph_mx)
        print(f"Матрица {args.count}×{args.count} "
                f"{'(симметричная) ' if args.symmetric else ''} "
                f"сохранена в файл '{args.output}'")
        return

    if args.input:
        n, graph_mx = load_mx(args.input)
    else:
        n: int = int(input())
        graph_mx: list[list[int]] = [[int(i) for i in input().split()] for _ in range(n)]

    if args.output:
        write_mx(args.output, graph_mx)
        print(f"Матрица {n}×{n} "
                f"{'(симметричная) ' if args.symmetric else ''} "
                f"сохранена в файл '{args.output}'")

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
