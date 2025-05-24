#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Данный модуль содержит реализацию точного решения задачи коммивояжера
через динамическое программирование.
"""
INF: float = float('inf')


def tsp_dp(n: int, graph: list[list[int]]) -> None:
    """
    Функция для решения задачи коммивояжёра методом динамического программирования.
    Алгоритм Хельда-Карпа.
    :param n: Количество городов
    :param graph: Матрица весов
    :return: None
    """
    dp: list[list[int | float]] = [[INF] * n for _ in range(1 << n)]
    parent: list[list[int]] = [[-1] * n for _ in range(1 << n)]
    dp[1][0]: int = 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or graph[u][v] == 0:
                    continue
                next_mask: int = mask | (1 << v)
                new_cost: int = dp[mask][u] + graph[u][v]
                if new_cost < dp[next_mask][v]:
                    dp[next_mask][v]: int = new_cost
                    parent[next_mask][v]: int = u

    full_mask: int = (1 << n) - 1
    min_cost: int | float = INF
    last: int = -1
    for i in range(1, n):
        if graph[i][0] != 0 and dp[full_mask][i] + graph[i][0] < min_cost:
            min_cost: int = dp[full_mask][i] + graph[i][0]
            last: int = i

    if min_cost == INF:
        print("no path")
        return

    path: list[int] = [0]
    mask: int = full_mask
    while last != -1:
        path.append(last)
        temp: int = parent[mask][last]
        mask ^= (1 << last)
        last: int = temp
    path.reverse()

    print(min_cost)
    print(" ".join(map(str, path)))
