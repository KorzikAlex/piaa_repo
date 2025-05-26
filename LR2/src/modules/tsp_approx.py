#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Данный модуль содержит реализацию приближенного решения задачи коммивояжера
через алгоритм лучшего соседа (на основе МОД).
"""
INF: float = float("inf")  # Бесконечность для инициализации расстояний


def prim_mst_cost(graph, nodes) -> int | float:
    """
    Функция для вычисления стоимости минимального остовного дерева
    с использованием алгоритма Прима.
    Приближённый алгоритм.
    :param graph: Матрица смежности графа
    :param nodes: Список вершин, для которых нужно найти MST
    :return: Стоимость MST или INF, если нет пути
    """
    print(f"\n  [MST] Начало расчета для узлов: {nodes}")
    visited: list[bool] = [False] * len(graph)
    min_edge: list[int | float] = [INF] * len(graph)
    min_edge[nodes[0]]: int = 0  # Стартовая вершина
    total: int = 0

    for step in range(len(nodes)):
        u: int = -1
        for v in nodes:
            if not visited[v] and (u == -1 or min_edge[v] < min_edge[u]):
                u: int = v
        print(f"  [MST] Шаг {step + 1}: Выбрана вершина {u} с весом {min_edge[u]}")
        if min_edge[u] == INF:
            print("  [MST] Невозможно построить MST!")
            return INF
        visited[u]: bool = True
        total += min_edge[u]
        print(f"  [MST] Добавлено в MST: {u}, текущая стоимость: {total}")
        for v in nodes:
            if graph[u][v] != 0 and not visited[v]:
                new_weight: int = graph[u][v]
                if new_weight < min_edge[v]:
                    print(f"  [MST] Обновлен вес для вершины {v} -> {graph[u][v]}")
                    min_edge[v]: int = new_weight
    print(f"  [MST] Итоговая стоимость MST: {total}\n")
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

    path: list[int] = [0]  # Начинаем со стартовой вершины
    total_cost: int = 0
    current: int = 0

    print("Начало алгоритма. Стартовый город: 0")
    for step in range(n - 1):  # Последовательно добавляем лучший следующий город
        print(f"\nШаг {step + 1}: Текущий путь: {' → '.join(map(str, path))}")
        print(f"Текущая стоимость: {total_cost}")
        print(f"Ищем следующий город из {current}...")

        best_next: int = -1
        best_cost: float = INF
        for v in range(n):
            if not visited[v] and graph[current][v] != 0:
                remaining: list[int] = [i for i in range(n) if not visited[i] and i != v]
                l_bound: int | float = prim_mst_cost(graph, remaining) if remaining else 0
                cost: int | float = graph[current][v] + l_bound
                print(
                    f"  Город {v}: стоимость перехода={graph[current][v]}, "
                    f"оценка MST={l_bound}, общая оценка={cost}"
                )
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

    # Завершаем цикл, возвращаясь в стартовый город
    print(f"\nФинальный переход из {current} в стартовый город 0")
    if graph[current][0] == 0:
        print("no path")
        return
    total_cost += graph[current][0]
    path.append(0)
    print("\nРезультат:")
    print(total_cost)
    print(" ".join(map(str, path)))
