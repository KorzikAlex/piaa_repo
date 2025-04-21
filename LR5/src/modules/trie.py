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
    alphabet: dict = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3,
        'N': 4
    }
    return alphabet[c]


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
        self.__vertices: list[Vertex] = [Vertex(0, alpha, None, None)]
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

    def find(self, s: str) -> bool:
        """
        Проверяет, есть ли строка в дереве.
        :param s: Строка для поиска.
        :return: True, если строка найдена, иначе False.
        """
        v: Vertex = self.root
        for char in s:
            idx: int = _num(char)
            if v.next[idx] is None:
                return False
            v: Vertex = v.next[idx]
        return v.is_terminal

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
        :param v:
        :param c:
        :return:
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
