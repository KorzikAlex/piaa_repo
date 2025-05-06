# *- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 2.
МВиГ: Алгоритм Литтла с модификацией: после приведения матрицы, к нижней
оценке веса решения добавляется нижняя оценка суммарного веса остатка пути на
основе МОД. Приближённый алгоритм: АБС.
Начинать АБС со стартовой вершины.
"""
from pprint import pprint


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    n: int = int(input())
    matrix: list[list[int]] = [[int(i) for i in input().split()] for _ in range(n)]
    matrix_2: list[list[float]] = [[float(i) for i in input().split()] for _ in range(n)]
    print(n)
    pprint(matrix)
    pprint(matrix_2)


if __name__ == '__main__':
    main()
