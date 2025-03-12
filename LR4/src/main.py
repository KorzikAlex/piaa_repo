"""
Главный файл для выполнения заданий.
"""

from modules.kmp import kmp_search


def main1() -> None:
    """
    Функция для выполнения задания 1
    :return:
    """
    p: str = input()
    t: str = input()
    print(kmp_search(t, p))


def main2() -> None:
    """
    Функция для выполнения задания 2
    :return:
    """
    pass


if __name__ == "__main__":
    main1()
