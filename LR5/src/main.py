# -*- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 2.
Подсчитать количество вершин в автомате;
Вывести список найденных образцов,
имеющих пересечения с другими найденными образцами в строке поиска.
"""
from modules.trie import Trie
from modules.vertex import Vertex


def aho_corasick_search():
    """
    Алгоритм Ахо-Корасика для поиска всех образцов в тексте.
    :return: None
    """
    alpha: int = 5
    text: str = input().strip()
    n: int = int(input())
    patterns: list[str] = []
    lengths: list[int] = []
    trie: Trie = Trie(alpha)
    for idx in range(n):
        pattern = input().strip()
        patterns.append(pattern)
        trie.add(pattern, idx + 1)  # Нумерация шаблонов с 1
        lengths.append(len(pattern))

    occurrences: list[tuple[int, int]] = []
    current: Vertex = trie.root
    for i in range(len(text)):
        c: str = text[i]
        current: Vertex = trie.go(current, c)
        v: Vertex = current
        while v != trie.root:
            if v.is_terminal:
                for p_num in v.pattern_numbers:
                    start: int = i - lengths[p_num - 1] + 1  # lengths[0] соответствует шаблону 1
                    if start >= 0:
                        occurrences.append((start + 1, p_num))  # Переводим в 1-based индекс
            v: Vertex = trie.get_link(v)

    # Сортировка и вывод
    occurrences.sort(key=lambda x: (x[0], x[1]))
    pos: int
    p: int
    for pos, p in occurrences:
        print(pos, p)


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    print("Задание #1: Нахождение всех образцов в тексте")
    aho_corasick_search()

    print("Задание #2: Решение задачи точного поиска одного образца с джокером")


if __name__ == '__main__':
    main()
