"""
Этот модуль содержит алгоритм Кнута-Морриса-Пратта и необходимые для него функции.
"""


def prefix_function(text: str) -> list[int]:
    """
    Функция для поиска префикс-функции строки (векторный формат)
    :param text:
    :return:
    """
    n: int = len(text)
    pi: list[int] = [0] * n
    for i in range(1, n):
        j: int = pi[i - 1]
        while j > 0 and text[j] != text[i]:
            j = pi[j - 1]
        if text[i] == text[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text: str, sub_text: str, start_index=0) -> int:
    """
    Функция для поиска подстроки в строке
    :param text:
    :param sub_text:
    :param start_index:
    :return:
    """
    j: int = 0
    pi: list[int] = prefix_function(sub_text)
    for i in range(start_index, len(text)):
        while j > 0 and text[i] != sub_text[j]:
            j = pi[j - 1]
        if text[i] == sub_text[j]:
            j += 1
        if j >= len(sub_text):
            return i - j + 1
    return -1


def find_cyclic_shift(text: str, sub_text: str) -> int:
    """
    Функция для поиска циклического сдвига строки
    :param text:
    :param sub_text:
    :return:
    """
    return -1
