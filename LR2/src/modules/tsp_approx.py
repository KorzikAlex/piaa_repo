#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Данный модуль содержит реализацию приближенного решения задачи коммивояжера
через алгоритм лучшего соседа (на основе МОД).
"""
INF: float = float('inf')


def prim_mst_cost(graph, nodes) -> int | float:
    """
    Функция для вычисления стоимости минимального остовного дерева (MST)
    с использованием алгоритма Прима.
    :param graph: Матрица смежности графа
    :param nodes: Список вершин, для которых нужно найти MST
    :return: Стоимость MST или INF, если нет пути
    """
    visited: list[bool] = [False] * len(graph)
    min_edge: list[int | float] = [INF] * len(graph)
    min_edge[nodes[0]]: int = 0
    total: int = 0

    for _ in range(len(nodes)):
        u: int = -1
        for v in nodes:
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u: int = v
        if min_edge[u] == INF:
            return INF
        visited[u]: bool = True
        total += min_edge[u]
        for v in nodes:
            if graph[u][v] != 0 and not visited[v]:
                min_edge[v]: int = min(min_edge[v], graph[u][v])
    return total


def tsp_alsh2(n: int, graph: list[list[int]]) -> None:
    """
    Функция для решения задачи коммивояжёра методом АЛШ-2 (Алгоритм лучшего соседа).
    :param n: Количество городов
    :param graph: Матрица весов
    :return: None
    """
    visited: list[bool] = [False] * n
    visited[0]: int = True

    path: list[int] = [0]
    total_cost: int = 0
    current: int = 0

    for _ in range(n - 1):
        best_next: int = -1
        best_cost: float = INF
        for v in range(n):
            if not visited[v] and graph[current][v] != 0:
                remaining: list[int] = [i for i in range(n) if not visited[i] and i != v]
                l_bound: int | float = prim_mst_cost(graph, remaining) if remaining else 0
                cost: int | float = graph[current][v] + l_bound
                if cost < best_cost:
                    best_cost: int = cost
                    best_next: int = v
        if best_next == -1:
            print("no path")
            return
        total_cost += graph[current][best_next]
        current: int = best_next
        path.append(current)
        visited[current]: bool = True

    if graph[current][0] == 0:
        print("no path")
        return
    total_cost += graph[current][0]
    path.append(0)

    print(total_cost)
    print(" ".join(map(str, path)))
