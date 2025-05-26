#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 8 Точный метод: динамическое программирование (не МВиГ), итеративная
реализация.
Приближённый алгоритм: АЛШ-2.
Требование перед сдачей: прохождение кода в задании 3.1 на Stepik.
Замечание к варианту 8: АЛШ-2 начинать со стартовой вершины.
"""
from argparse import Namespace

from modules.tsp_exact import tsp_dp
from modules.tsp_approx import tsp_alsh2

from modules.loader import load_mx, write_mx, generate_mx
from modules.parser import get_args


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    args: Namespace = get_args()

    # Генерация матрицы
    if args.generate:
        file_name: str = args.output
        n: int = args.count
        if not 5 <= args.count <= 15:
            print("Значение аргумента должно быть в диапазоне [5, 15].")
            return
        graph_mx: list[list[int]] = generate_mx(n, args.symmetric)
        if args.output:
            file_name = args.output
        try:
            write_mx(file_name, graph_mx)
        except IOError:
            print(f"Ошибка записи в файл '{file_name}'. Проверьте права доступа.")
            return
        print(
            f"Матрица {n}×{n}"
            f"{' (симметричная)' if args.symmetric else ''} "
            f"сохранена в файл '{file_name}'"
        )
        return

    if args.input:
        # Чтение из файла
        try:
            n, graph_mx = load_mx(args.input)
        except FileNotFoundError:
            print(f"Файл '{args.input}' не найден.")
            return
        except ValueError:
            print("Неверный формат файла.")
            return
    else:
        # Чтение с stdin
        n: int = int(input())
        graph_mx: list[list[int]] = [[int(i) for i in input().split()] for _ in range(n)]

    # Выбор метода решения
    if args.method == "exact":
        # Точный метод
        tsp_dp(n, graph_mx)
    elif args.method == "approx":
        # Приближённый алгоритм
        tsp_alsh2(n, graph_mx)
    else:
        # Неизвестный метод
        print(
            "Неизвестный метод решения задачи коммивояжёра. "
            "Используйте 'exact' или 'approx'."
        )
        return


if __name__ == '__main__':
    main()
