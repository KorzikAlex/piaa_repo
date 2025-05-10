# *- coding: utf-8 -*-
"""
Файл, содержащий функции для решения задачи о коммивояжере.
"""


def fill_dp(n: int, graph_mx: list[list[int]]) -> tuple[list[list[int | float]], list[list[int]]]:
    """
    Функция для заполнения таблицы dp и таблицы родителей.
    :return: Таблица dp
    """
    dp: list[list[int | float]] = [[float("inf")] * n for _ in range(1 << n)]
    parent: list[list[int]] = [[-1] * n for _ in range(1 << n)]
    dp[1][0]: int | float = 0
    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)) or dp[mask][u] == float("inf"):
                continue
            # Перебираем все возможные следующие города
            for v in range(n):
                if v == u or (mask & (1 << v)) or graph_mx[u][v] == 0:
                    continue
                new_mask: int = mask | (1 << v)
                new_cost: int = dp[mask][u] + graph_mx[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v]: int = new_cost
                    parent[new_mask][v]: int = u
    return dp, parent


def calc_best_path(n: int, dp: list[list[int | float]],
                    graph_mx: list[list[int]]) -> tuple[int, int]:
    """
    Находит лучший путь из всех возможных путей.
    :return: Количество городов и лучший город для возврата.
    """
    full_mask: int = (1 << n) - 1
    min_total: float | int = float("inf")
    best_u: int = -1
    for u in range(n):
        if u == 0:
            continue  # Пропускаем, так как нельзя остаться в 0 для возврата
        if graph_mx[u][0] > 0 and (full_mask & (1 << u)):
            total: int = dp[full_mask][u] + graph_mx[u][0]
            if total < min_total:
                min_total: float | int = total
                best_u: int = u
    return min_total, best_u


def restore_path(n: int, parent: list[list[int]], best_u: int) -> list[int]:
    """
    Восстанавливает путь из таблицы родителей.
    :return: Путь из таблицы родителей.
    """
    # Восстановление пути
    full_mask: int = (1 << n) - 1
    path: list[int] = []
    current_u: int = best_u
    current_mask: int = full_mask
    # Собираем путь от best_u до 0
    while current_mask != 1:
        path.append(current_u)
        prev_u: int = parent[current_mask][current_u]
        current_mask ^= (1 << current_u)
        current_u: int = prev_u
    path.append(current_u)  # Добавляем начальный город 0
    path.reverse()
    path.append(0)  # Добавляем 0 в конец для завершения цикла
    return path
