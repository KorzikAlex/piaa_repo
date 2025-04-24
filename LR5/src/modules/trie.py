# -*- coding: utf-8 -*-
"""
Класс Trie для работы с префиксными деревьями.
"""
from modules.vertex import Vertex


def _num(c: str) -> int:
    """
    Функция для получения номера буквы в алфавите.
    :param c: Буква
    :return: Номер буквы
    """
    alphabet: dict[str, int] = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3,
        'N': 4
    }
    return alphabet[c]


def find_overlaps(occurrences: list[tuple[int, int, int]]) -> list[int]:
    """
    Возвращает список уникальных номеров
    :param occurrences:
    """
    # Предполагаем, что occurrences уже отсортирован по (start, end)
    overlaps: set = set()
    for i in range(len(occurrences) - 1):
        s1: int
        e1: int
        p1: int
        s1, e1, p1 = occurrences[i]

        s2: int
        e2: int
        p2: int
        s2, e2, p2 = occurrences[i + 1]
        if e1 >= s2:
            overlaps.add(p1)
            overlaps.add(p2)
    # Возвращаем уже отсортированный список уникальных номеров
    return sorted(overlaps)


class Trie:
    """
    Класс Trie для работы с префиксными деревьями.
    """

    def __init__(self, alpha: int) -> None:
        """
        Конструктор класса Trie.
        :param alpha: Размер алфавита бора.
        """
        self.__alpha: int = alpha
        self.__vertices: list[Vertex] = [Vertex(0, alpha)]
        self.__root: Vertex = self.vertices[0]

    @property
    def size(self) -> int:
        """
        Возвращает количество вершин в дереве.
        :return: Количество вершин в дереве.
        """
        return len(self.vertices)

    @property
    def last(self) -> Vertex:
        """
        Возвращает последнюю вершину в дереве.
        :return: Последняя вершина в дереве.
        """
        return self.vertices[-1]

    @property
    def alpha(self):
        """
        Возвращает размер алфавита.
        :return: Размер алфавита.
        """
        return self.__alpha

    @property
    def vertices(self) -> list[Vertex]:
        """
        Возвращает список вершин в дереве.
        :return: Список вершин в дереве.
        """
        return self.__vertices

    @property
    def root(self) -> Vertex:
        """
        Возвращает корень дерева.
        :return: Корень дерева.
        """
        return self.__root

    def add(self, s: str, pattern_num: int) -> None:
        """
        Добавляет строку в дерево.
        :param s: Строка для добавления.
        :param pattern_num: Номер шаблона.
        :return: None
        """
        v: Vertex = self.root
        char: str
        for char in s:
            idx: int = _num(char)
            if v.next[idx] is None:
                self.vertices.append(Vertex(self.size, self.alpha, v, char))
                v.next[idx] = self.last
            v = v.next[idx]
        v.is_terminal = True
        v.pattern_numbers.append(pattern_num)

    def search(self, s: str) -> list[tuple[int, int]]:
        """
        Проверяет, есть ли строка в дереве.
        :param s: Строка для поиска.
        :return: Список кортежей (позиция, номер шаблона), где позиция - это индекс в строке s,
        """
        res: list[tuple[int, int]] = []
        v: Vertex = self.root

        i: int
        char: str
        for i, char in enumerate(s):
            v = self.go(v, char)
            while v is not self.root:
                if v.is_terminal:
                    for pid in v.pattern_numbers:
                        res.append((i, pid))
                v = self.get_link(v)
        return res

    def get_link(self, v: Vertex) -> Vertex:
        """
        Возвращает суффиксную ссылку для вершины v.
        :param v: Вершина, для которой нужно получить суффиксную ссылку.
        :return: Суффиксная ссылка для вершины v.
        """
        if v.sufflink is None:
            if self.root in (v, v.parent):
                v.sufflink = self.root
            else:
                v.sufflink = self.go(self.get_link(v.parent), v.pchar)
        return v.sufflink

    def go(self, v: Vertex, c: str) -> Vertex:
        """
        Возвращает вершину, в которую ведет переход по символу c из вершины v.
        :param v: Вершина, из которой нужно сделать переход.
        :param c: Символ, по которому нужно сделать переход.
        :return: Вершина, в которую ведет переход по символу c из вершины v.
        """
        idx = _num(c)
        if v.go[idx] is None:
            if v.next[idx] is not None:
                v.go[idx] = v.next[idx]
            elif v == self.root:
                v.go[idx] = self.root
            else:
                v.go[idx] = self.go(self.get_link(v), c)
        return v.go[idx]
