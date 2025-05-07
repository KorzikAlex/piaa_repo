# -*- coding: utf-8 -*-
"""
Главный файл программы.

Вариант 7.
Вывод графического представления автомата.
"""
from modules.trie import Trie
from modules.vertex import Vertex


def visualize_and_print(trie: Trie, filename: str) -> None:
    """
    Выводит информацию о вершинах и графическое представление автомата.
    :param trie: Построенный автомат
    :param filename: Имя файла с графическим представлением
    :return: None
    """
    trie.print_bor_structure()
    print("\nВычисление оставшихся суффиксных ссылок")
    trie.precompute_sufflinks()  # вычисление всех суффиксных ссылок
    trie.print_automaton_structure()
    trie.visualize(filename)  # создание графического представления автомата
    # Подсчет и вывод числа вершин
    print("Количество вершин в автомате:", trie.size)


def aho_corasick_search() -> None:
    """
    Алгоритм Ахо-Корасик для поиска всех образцов в тексте.
    :return: None
    """
    text: str = input().strip()  # текст для поиска
    n: int = int(input())  # количество образцов
    patterns: list[str] = []  # список образцов
    lengths: list[int] = []  # длины образцов
    trie: Trie = Trie()  # создание префиксного дерева (Бора)
    for i in range(n):
        pattern: str = input().strip()  # считывание образца
        patterns.append(pattern)  # добавление образца в список
        lengths.append(len(pattern))  # добавление длины образца в список
    i: int
    pattern: str
    for i, pattern in enumerate(patterns):
        trie.add(pattern, i + 1)  # Нумерация шаблонов с 1

    # Поиск образцов в тексте
    print("\nНачало поиска в тексте:")
    occ: list[tuple[int, int]] = []  # список для хранения найденных образцов
    current: Vertex = trie.root  # текущая вершина
    for i, char in enumerate(text):
        current: Vertex = trie.go(current, char)  # переход по ребру
        print(f"\nШаг {i + 1}: Символ '{char}'")
        print(f"Текущая вершина: {current.id}")
        print(current)
        v: Vertex = current  # текущая вершина
        while v != trie.root:  # пока не достигли корня
            if v.is_terminal:  # если вершина терминальная
                print(f"\tНайдена терминальная вершина {v.id} с шаблонами {v.pattern_numbers}")
                for p_num in v.pattern_numbers:  # для каждого номера образца
                    start: int = i - lengths[p_num - 1] + 1  # начало образца
                    if start >= 0:
                        occ.append((start + 1, p_num))  # Переводим в 1-based индекс
            v: Vertex = trie.get_link(v)  # переход по суффиксной ссылке

    # Сортировка и вывод
    occ.sort(key=lambda x: (x[0], x[1]))

    visualize_and_print(trie, "aho_corasick_automaton")

    print("\nРезультаты поиска:")
    pos: int
    p: int
    for pos, p in occ:
        print(f"Позиция {pos}, образец {p}")


def search_with_wildcard() -> None:
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
    print("\nСегменты для поиска:")
    pid: int
    seg: str
    off: int
    for pid, (seg, off) in enumerate(segments):
        print(f"Сегмент {pid + 1}: '{seg}' начинается с позиции {off + 1}")
        trie.add(seg, pid)  # добавление сегмента в префиксное дерево

    occ: list[tuple[int, int]] = trie.search(text)  # поиск образцов в тексте
    needed: int = len(segments)  # количество сегментов
    counts: list[int] = [0] * (len_text - len_pattern + 1 if len_text >= len_pattern else 0)  # инициализация счетчиков

    end_pos: int
    pid: int
    for end_pos, pid in occ:
        seg: str
        off: int
        seg, off = segments[pid]  # получение сегмента и его смещения
        print(f"Сегмент '{seg}' (PID {pid}) найден на позиции {end_pos - len(seg) + 1}-{end_pos}")
        l: int = len(seg)  # длина сегмента
        p: int = end_pos - (off + l - 1)  # вычисление позиции
        if 0 <= p <= len_text - len_pattern:
            counts[p] += 1  # увеличение счетчика для позиции p
    visualize_and_print(trie, "aho_corasick_wildcard_automaton")

    print("\nПозиции с полным совпадением:")
    i: int
    c: int
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


if __name__ == "__main__":
    main()
