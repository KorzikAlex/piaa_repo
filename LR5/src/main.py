# -*- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 2.
Подсчитать количество вершин в автомате;
Вывести список найденных образцов,
имеющих пересечения с другими найденными образцами в строке поиска.
"""
from modules.trie import Trie, find_overlaps
from modules.vertex import Vertex


def aho_corasick_search():
    """
    Алгоритм Ахо-Корасика для поиска всех образцов в тексте.
    :return: None
    """
    alpha: int = 5  # размер алфавита
    text: str = input().strip()  # текст для поиска
    n: int = int(input())  # количество образцов
    patterns: list[str] = []  # список образцов
    lengths: list[int] = []  # длины образцов
    trie: Trie = Trie(alpha)  # создание префиксного дерева (Бора)
    for idx in range(n):
        pattern = input().strip()  # считывание образца
        patterns.append(pattern)  # добавление образца в список
        trie.add(pattern, idx + 1)  # Нумерация шаблонов с 1
        lengths.append(len(pattern))  # добавление длины образца в список

    # Подсчет и вывод числа вершин
    print("Количество вершин в автомате:", trie.size)

    occurrences: list[tuple[int, int]] = []
    current: Vertex = trie.root
    for i in range(len(text)):
        c: str = text[i]
        current: Vertex = trie.go(current, c)
        v: Vertex = current
        while v != trie.root:
            if v.is_terminal:
                for p_num in v.pattern_numbers:
                    start: int = i - lengths[p_num - 1] + 1
                    if start >= 0:
                        occurrences.append((start + 1, p_num))  # Переводим в 1-based индекс
            v: Vertex = trie.get_link(v)

    # Сортировка и вывод
    occurrences.sort(key=lambda x: (x[0], x[1]))

    pos: int
    p: int
    for pos, p in occurrences:
        print(pos, p)

    # overlaps: list[int] = find_overlaps(occurrences)
    # print("Шаблоны, имеющие пересечения:", overlaps)


def search_with_wildcard():
    """
    Поиск с учетом джокера.
    :return: None
    """
    text: str = input().strip()
    pattern: str = input().strip()
    wildcard: str = input().strip()
    len_text, len_pattern = len(text), len(pattern)

    segments: list[tuple[str, int]] = []
    curr: list[str] = []
    start: int = 0
    i: int
    ch: str
    for i, ch in enumerate(pattern):
        if ch == wildcard:
            if curr:
                segments.append(("".join(curr), start))
                curr: list[str] = []
            start: int = i + 1
        else:
            if not curr:
                start: int = i
            curr.append(ch)
    if curr:
        segments.append(("".join(curr), start))

    trie: Trie = Trie(5)
    pid: int
    seg: str
    off: int
    for pid, (seg, off) in enumerate(segments):
        trie.add(seg, pid)

    # Подсчет и вывод числа вершин
    print("Количество вершин в автомате:", trie.size)

    occ: list[tuple[int, int]] = trie.search(text)
    needed: int = len(segments)
    counts: list[int] = [0] * (len_text - len_pattern + 1 if len_text >= len_pattern else 0)

    end_pos: int
    pid: int
    for end_pos, pid in occ:
        seg, off = segments[pid]
        l: int = len(seg)
        p: int = end_pos - (off + l - 1)
        if 0 <= p <= len_text - len_pattern:
            counts[p] += 1

    for i, c in enumerate(counts):
        if c == needed:
            print(i + 1)


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
