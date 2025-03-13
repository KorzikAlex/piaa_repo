"""
Главный файл для выполнения заданий.
"""

from modules.kmp import kmp_search, find_cyclic_shift


def main1() -> None:
    """
    Функция для выполнения задания 1 (найти все индексы вхождения подстроки в строку).
    :return:
    """
    p: str = input()  # вводим подстроку
    t: str = input()  # вводим строку
    print(*kmp_search(t, p), sep=",")  # выводим результат


def main2() -> None:
    """
    Функция для выполнения задания 2.
    :return:
    """
    a: str = input()  # вводим строку a
    b: str = input()  # вводим строку b
    print(find_cyclic_shift(a, b))  # выводим результат


if __name__ == "__main__":
    main1()  # вызов функции main1()
    main2()  # вызов функции main2()
