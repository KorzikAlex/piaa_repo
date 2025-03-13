"""
Этот модуль содержит алгоритм Кнута-Морриса-Пратта и необходимые для него функции.
"""


def prefix_func(text: str) -> list[int]:
    """
    Функция для поиска префикс-функции строки (векторный формат)
    :param text:
    :return:
    """
    n: int = len(text)
    pi: list[int] = [0] * n
    for i in range(1, n):
        j: int = pi[i - 1]
        while (j > 0) and (text[j] != text[i]):
            j: int = pi[j - 1]
        if text[i] == text[j]:
            j += 1
        pi[i]: int = j
    return pi


def kmp_search(text: str, sub_text: str, start_index: int = 0) -> list[int]:
    """
    Функция для поиска подстроки в строке
    :param text:
    :param sub_text:
    :param start_index:
    :return:
    """
    result_indexes: list[int] = [] # список для хранения индексов вхождения подстроки
    j: int = 0
    pi: list[int] = prefix_func(sub_text) # префикс-функция подстроки
    for i in range(start_index, len(text)):
        while (j > 0) and (text[i] != sub_text[j]):
            j: int = pi[j - 1]
        if text[i] == sub_text[j]:
            j += 1
        if j >= len(sub_text):
            result_indexes.append(i - j + 1)
            j: int = pi[j - 1]
    if not result_indexes: # если список пуст, то возвращаем -1
        return [-1]
    return result_indexes # иначе возвращаем список индексов


def find_cyclic_shift(text: str, sub_text: str) -> int:
    """
    Функция для поиска циклического сдвига строки
    :param text:
    :param sub_text:
    :return:
    """
    if len(text) == 0 or len(sub_text) == 0:
        return -1
    j: int = 0
    pi: list[int] = prefix_func(sub_text)
    for i in range(2 * len(text)):
        idx: int = i % len(text)
        while (j > 0) and (text[idx] != sub_text[j]):
            j: int = pi[j - 1]
        if text[idx] == sub_text[j]:
            j += 1
        if j == len(sub_text):
            return i - j + 1
    return -1
