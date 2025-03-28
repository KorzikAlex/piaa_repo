"""
Главный файл программы.
"""
from modules.vagner_fisher import calculate_edit_distance, compute_edit_sequence


def main() -> None:
    """
    Главная функция
    :return:
    """
    print("Задание #1: Алгоритм Вагнера-Фишера")
    rep_cost, ins_cost, del_cost = map(int, input().split())
    s1 = input()
    s2 = input()
    print(calculate_edit_distance(s1, s2, rep_cost, ins_cost, del_cost))

    print("Задание #2: Алгоритм Вагнера-Фишера. Порядок операции")
    rep_cost, ins_cost, del_cost = map(int, input().split())
    s1: str = input()
    s2: str = input()
    print(compute_edit_sequence(s1, s2, rep_cost, ins_cost, del_cost), s1, s2, sep="\n")

    print("Задание #3: Расстояние Левенштейна")
    s1: str = input()
    s2: str = input()
    print(calculate_edit_distance(s1, s2))


if __name__ == "__main__":
    main()
