#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Данный модуль содержит реализацию точного решения задачи коммивояжера
через динамическое программирование.
"""
INF: float = float("inf")  # Бесконечность для инициализации расстояний


def tsp_dp(n: int, graph: list[list[int]]) -> None:
    """
    Функция для решения задачи коммивояжёра методом динамического программирования.
    Итеративная реализация.
    Алгоритм Хельда-Карпа.
    :param n: Количество городов
    :param graph: Матрица весов
    :return: None
    """
    # Инициализация таблиц DP и предков
    dp: list[list[int | float]] = [[INF] * n for _ in range(1 << n)]
    parent: list[list[int]] = [[-1] * n for _ in range(1 << n)]
    print("Инициализация DP таблицы. Начальная точка 0 с стоимостью 0")
    dp[1][0]: int = 0  # Стартуем из города 0

    # Перебор всех подмножеств вершин
    print("\nЭтапы обновления путей:")
    for mask in range(1 << n):
        print(f"\nОбработка маски: {bin(mask)}")
        for u in range(n):
            if not (mask & (1 << u)):
                print(f"  Город {u} не в маске — пропуск")
                continue
            print(f"  Текущий город u={u}")
            for v in range(n):
                if mask & (1 << v) or graph[u][v] == 0:
                    print(f"  Город v={v} уже в маске")
                    continue
                if graph[u][v] == 0:
                    print(f"    Нет пути из {u} в {v} — пропуск")
                    continue
                next_mask: int = mask | (1 << v)
                new_cost: int = dp[mask][u] + graph[u][v]
                print(
                    f"    Проверка перехода u={u} -> v={v}: next_mask={bin(next_mask)}, "
                    f"возможная стоимость={new_cost} (текущая dp={dp[next_mask][v]})"
                )
                if new_cost < dp[next_mask][v]:
                    dp[next_mask][v]: int = new_cost
                    parent[next_mask][v]: int = u
                    print(f"    Обновление: dp[{bin(next_mask)}][{v}] = {new_cost}, parent={u}")

    # Поиск минимального пути возвращения в начальный город
    full_mask: int = (1 << n) - 1
    min_cost: int | float = INF
    last: int = -1
    print("\nПоиск минимального пути возврата в город 0:")
    for i in range(1, n):
        cost: int | float = dp[full_mask][i] + graph[i][0] if graph[i][0] != 0 else INF
        print(f"  Город {i}: стоимость пути через него = {cost}")
        if cost < min_cost:
            min_cost: int = dp[full_mask][i] + graph[i][0]
            last: int = i

    # Если не найден путь, выводим сообщение (наименьшая стоимость остаётся бесконечностью)
    if min_cost == INF:
        print("no path")
        return

    # Восстановление пути
    print(f"\nМинимальная стоимость: {min_cost}")
    print("Восстановление пути:")
    path: list[int] = [0]
    mask: int = full_mask
    while last != -1:
        print(f"  Текущий узел: {last}, маска: {bin(mask)}")
        path.append(last)
        temp: int = parent[mask][last]
        mask ^= (1 << last)
        last: int = temp
    path.reverse()

    print("\nРезультат:")
    print(min_cost)
    print(" ".join(map(str, path)))
