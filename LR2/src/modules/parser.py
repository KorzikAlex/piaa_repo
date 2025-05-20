#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Это файл для парсинга аргументов командной строки.
"""
import argparse


def get_args():
    """
    Получить аргументы командной строки.
    :return: Аргументы командной строки
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=(
            "description:\n"
            "Решение задачи коммивояжёра двумя методами:\n"
            "    1) Точный (ДП, рекурсивно, старт из 0)\n"
            "    2) Приближённый (АЛШ-2, вариант 8)\n"
            "Кроме того, можно сгенерировать матрицу (произвольную или симметричную),\n"
            "сохранить её в файл и затем читать из файла."
        ),
        epilog=(
            "epilog:\n"
            "ДП (DP) - Динамическое программирование\n"
            "АЛШ-2 - Алгоритм лучшего соседа \n"
            "В файле матрицы весов на первой строке указывается количество городов (n), "
            "на следующих n строках — матрица.\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-i", "--input", type=str, dest="input",
                        help=(
                            "Имя файла с матрицей. "
                            "Если не указан, читаем из stdin."
                        ))
    parser.add_argument("-o", "--output", type=str, dest="output", default="output.txt",
                        help="Имя файла, в который сохраняем матрицу. По умолчанию output.txt.")
    parser.add_argument("-g", "--generate", action="store_true", dest="generate",
                        help="Сгенерировать новую матрицу весов.")
    parser.add_argument("-c", "--count", type=int, default=10, dest="count",
                        help="Количество городов (5 ≤ n ≤ 15). По умолчанию 10.")
    parser.add_argument("-s", "--symmetric", action="store_true", dest="symmetric",
                        help="Сгенерировать симметричную матрицу. По умолчанию нет.")
    parser.add_argument("--max-weight", type=int, default=100, dest="max_weight",
                        help="Максимальный вес ребра. По умолчанию 100.")
    parser.add_argument("--method", choices=["exact", "approx"], default="exact",
                        help=(
                            "Метод решения: exact — точный (DP), "
                            "approx — приближённый (АЛШ-2). "
                            "По умолчанию exact."
                        ))
    args = parser.parse_args()
    return args
