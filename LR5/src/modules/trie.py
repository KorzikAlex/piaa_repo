"""
Класс Trie для работы с префиксными деревьями.
"""
from vertex import Vertex


def num(c: str) -> int:
    """
    Функция для получения номера буквы в алфавите.
    :param c: Буква
    :return: Номер буквы
    """
    alphabet: dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'N': 4}
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
        self.alpha: int = alpha
        self.vertices: list[Vertex] = [Vertex(0, alpha, None, None)]
        self.root: Vertex = self.vertices[0]

    @property
    def size(self) -> int:
        """
        Возвращает количество вершин в дереве.
        :return: Количество вершин в дереве.
        """
        return len(self.vertices)

    @property
    def last(self):
        """
        Возвращает последнюю вершину в дереве.
        :return: Последняя вершина в дереве.
        """
        return self.vertices[-1]

    def add(self, s: str) -> None:
        """
        Добавляет строку в дерево.
        :param s: Строка для добавления.
        :return: None
        """
        v: Vertex = self.root
        for i in range(len(s)):
            idx = num(s[i])
            if v.next[num(s[i])] is None:
                self.vertices.append(Vertex(self.size, self.alpha, v, s[i]))
                v.next[num(s[i])] = self.last
            v = v.next[num(s[i])]
        v.is_terminal = True

    def find(self, s) -> bool:
        """
        Проверяет, есть ли строка в дереве.
        :param s: Строка для поиска.
        :return: True, если строка найдена, иначе False.
        """
        v: Vertex = self.root
        for i in range(len(s)):
            if v.next[num(s[i])] is None:
                return False
            v = v.next[num(s[i])]
        return v.is_terminal

    def get_link(self, v: Vertex) -> Vertex:
        """
        Возвращает суффиксную ссылку для вершины v.
        :param v: Вершина, для которой нужно получить суффиксную ссылку.
        :return: Суффиксная ссылка для вершины v.
        """
        if v.sufflink is None:
            v.sufflink = self.root if v == self.root or v.parent == self.root \
                else self.go(self.get_link(v.parent), v.pchar)
        return v.sufflink

    def go(self, v: Vertex, c: str) -> Vertex:
        """
        Возвращает вершину, в которую ведет переход по символу c из вершины v.
        :param v:
        :param c:
        :return:
        """
        idx = num(c)
        if v.go[num(c)] is None:
            if v.next[num(c)] is not None:
                v.go[num(c)] = v.next[num(c)]
            elif v == self.root:
                v.go[num(c)] = self.get_link(v).go(c)
            else:
                v.go[num(c)] = self.go(self.get_link(v), c)
        return v.go[num(c)]
