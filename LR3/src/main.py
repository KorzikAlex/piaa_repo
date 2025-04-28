# -*- coding: utf-8 -*-
"""
Главный файл программы.

Вар. 3а. Добавляется 4-я операция со своей стоимостью: последовательная вставка
двух одинаковых символов.
"""
from modules.vagner_fisher import calculate_edit_distance, compute_edit_sequence


def main() -> None:
    """
    Главная функция
    :return:
    """
    print("Задание #1: Алгоритм Вагнера-Фишера")
    rep_cost, ins_cost, del_cost, ins2_cost = map(int, input().split())
    s1: str = input()
    s2: str = input()
    print("Результат:", calculate_edit_distance(s1, s2, rep_cost, ins_cost, del_cost, ins2_cost))

    print("Задание #2: Алгоритм Вагнера-Фишера. Порядок операции")
    rep_cost, ins_cost, del_cost, ins2_cost = map(int, input().split())
    s1: str = input()
    s2: str = input()
    print(compute_edit_sequence(s1, s2, rep_cost, ins_cost, del_cost, ins2_cost), s1, s2, sep="\n")

    print("Задание #3: Расстояние Левенштейна")
    s1: str = input()
    s2: str = input()
    print("Результат:", calculate_edit_distance(s1, s2))


if __name__ == "__main__":
    main()
