# -*- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 7.
Вывод графического представления автомата.
"""
from modules.trie import Trie
from modules.vertex import Vertex


def aho_corasick_search():
    """
    Алгоритм Ахо-Корасика для поиска всех образцов в тексте.
    :return: None
    """
    text: str = input().strip()  # текст для поиска
    n: int = int(input())  # количество образцов
    patterns: list[str] = []  # список образцов
    lengths: list[int] = []  # длины образцов
    trie: Trie = Trie()  # создание префиксного дерева (Бора)
    for idx in range(n):
        pattern = input().strip()  # считывание образца
        patterns.append(pattern)  # добавление образца в список
        trie.add(pattern, idx + 1)  # Нумерация шаблонов с 1
        lengths.append(len(pattern))  # добавление длины образца в список

    # Подсчет и вывод числа вершин
    print("Количество вершин в автомате:", trie.size)

    # Визуализация автомата
    trie.precompute_sufflinks()  # создание суффиксных ссылок
    trie.visualize("aho_corasick_automaton")  # создание графического представления автомата

    # Поиск образцов в тексте
    occurrences: list[tuple[int, int]] = []  # список для хранения найденных образцов
    current: Vertex = trie.root  # текущая вершина
    for i, c in enumerate(text):
        current: Vertex = trie.go(current, c)  # переход по ребру
        v: Vertex = current  # текущая вершина
        while v != trie.root:  # пока не достигли корня
            if v.is_terminal:  # если вершина терминальная
                for p_num in v.pattern_numbers:  # для каждого номера образца
                    start: int = i - lengths[p_num - 1] + 1  # начало образца
                    if start >= 0:
                        occurrences.append((start + 1, p_num))  # Переводим в 1-based индекс
            v: Vertex = trie.get_link(v)  # переход по суффиксной ссылке

    # Сортировка и вывод
    occurrences.sort(key=lambda x: (x[0], x[1]))

    pos: int
    p: int
    for pos, p in occurrences:
        print(pos, p)  # вывод позиций и номеров образцов


def search_with_wildcard():
    """
    Поиск с учетом джокера.
    :return: None
    """
    text: str = input().strip()  # текст для поиска
    pattern: str = input().strip()  # образец с джокером
    wildcard: str = input().strip()  # джокер
    len_text, len_pattern = len(text), len(pattern)  # длины текста и образца

    segments: list[tuple[str, int]] = []  # список сегментов
    curr: list[str] = []  # текущий сегмент
    start: int = 0  # начало сегмента
    i: int
    ch: str
    for i, ch in enumerate(pattern):
        if ch == wildcard:  # если символ - джокер
            if curr:
                segments.append(("".join(curr), start))  # добавление сегмента в список
                curr: list[str] = []  # очистка текущего сегмента
            start: int = i + 1  # обновление начала сегмента
        else:
            if not curr:
                start: int = i  # обновление начала сегмента
            curr.append(ch)  # добавление символа в текущий сегмент
    if curr:
        segments.append(("".join(curr), start))  # добавление последнего сегмента в список

    trie: Trie = Trie()  # создание префиксного дерева (Бора)
    pid: int
    seg: str
    off: int
    for pid, (seg, off) in enumerate(segments):
        trie.add(seg, pid)  # добавление сегмента в префиксное дерево

    # Подсчет и вывод числа вершин
    print("Количество вершин в автомате:", trie.size)

    # Визуализация автомата
    trie.precompute_sufflinks()  # создание суффиксных ссылок для каждой вершины
    trie.visualize("aho_corasick_wildcard_automaton")  # создание графического представления автомата

    occ: list[tuple[int, int]] = trie.search(text)  # поиск образцов в тексте
    needed: int = len(segments)  # количество сегментов
    counts: list[int] = [0] * (len_text - len_pattern + 1 if len_text >= len_pattern else 0)  # инициализация счетчиков

    end_pos: int
    pid: int
    for end_pos, pid in occ:
        seg: str
        off: int
        seg, off = segments[pid]  # получение сегмента и его смещения
        l: int = len(seg)  # длина сегмента
        p: int = end_pos - (off + l - 1)  # вычисление позиции
        if 0 <= p <= len_text - len_pattern:
            counts[p] += 1  # увеличение счетчика для позиции p

    for i, c in enumerate(counts):
        if c == needed:
            print(i + 1)  # вывод позиций, где все сегменты найдены


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    print("Задание #1: Нахождение всех образцов в тексте")
    aho_corasick_search()

    print("Задание #2: Решение задачи точного поиска одного образца с джокером")
    search_with_wildcard()


if __name__ == '__main__':
    main()
