# -*- coding: utf-8 -*-
"""
Класс Trie для работы с префиксными деревьями.
"""
from graphviz import Digraph

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


def _char(idx: int) -> str:
    """
    Функция для получения буквы по номеру.
    :param idx: Номер буквы
    :return: Буква
    """
    return ['A', 'C', 'G', 'T', 'N'][idx]


class Trie:
    """
    Класс Trie для работы с префиксными деревьями.
    """

    def __init__(self, alpha: int = 5) -> None:
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
    def alpha(self) -> int:
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
        Добавляет образец в дерево.
        :param s: Образец строки для добавления.
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
        :return: Список кортежей (позиция, номер шаблона), где позиция - это индекс в строке s
        """
        res: list[tuple[int, int]] = []
        v: Vertex = self.root

        i: int
        char: str
        for i, char in enumerate(s):
            v: Vertex = self.go(v, char)
            while v is not self.root:
                if v.is_terminal:
                    pid: int
                    for pid in v.pattern_numbers:
                        res.append((i, pid))
                v: Vertex = self.get_link(v)
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

    def go(self, v: Vertex, char: str) -> Vertex:
        """
        Возвращает вершину, в которую ведет переход по символу char из вершины v.
        :param v: Вершина, из которой нужно сделать переход.
        :param char: Символ, по которому нужно сделать переход.
        :return: Вершина, в которую ведет переход по символу char из вершины v.
        """
        idx: int = _num(char)
        v.go[idx]: Vertex
        if v.go[idx] is None:
            if v.next[idx] is not None:
                v.go[idx]: Vertex = v.next[idx]
            elif v == self.root:
                v.go[idx]: Vertex = self.root
            else:
                v.go[idx]: Vertex = self.go(self.get_link(v), char)
        return v.go[idx]

    def precompute_sufflinks(self) -> None:
        """
        Предварительно вычисляет суффиксные ссылки для всех вершин.
        :return: None
        """
        v: Vertex
        for v in self.vertices:
            self.get_link(v)

    def visualize(self, file_name: str = "aho_corasick") -> None:
        """
        Создает графическое представление автомата Ахо-Корасик и сохраняет его в файл.
        :param file_name: Имя файла для сохранения графа (без расширения).
        :return: None
        """
        dot: Digraph = Digraph(comment="Aho-Corasick Automaton")
        dot.attr(rankdir="TB", fontsize="14")  # Вертикальное расположение графа

        with dot.subgraph(name="cluster_automaton") as automaton:
            # Настройка графа
            automaton.attr(label="Автомат Ахо-Корасик", style="dotted")  # Название, стиль обводки

            # Добавление вершин
            v: Vertex
            for v in self.vertices:
                if v == self.root:
                    label = "root" + f" ({v.id})"
                else:
                    label = (v.pchar if v.pchar is not None else '') + f" ({v.id})"
                if v.is_terminal:
                    automaton.node(str(v.id), label, shape="circle", style="filled", fillcolor="lightblue")
                else:
                    automaton.node(str(v.id), label, shape="circle")

            # Добавление переходов
            for v in self.vertices:
                for _, next_v in enumerate(v.next):
                    if next_v is not None:
                        automaton.edge(str(v.id), str(next_v.id))  # Без метки

            # Добавление суффиксных ссылок
            for v in self.vertices:
                if v.sufflink is not None and v.sufflink != v:
                    automaton.edge(str(v.id), str(v.sufflink.id), style="dashed", color="red", constraint="false")

        with dot.subgraph(name="cluster_legend") as legend:
            # Добавление легенды
            legend.attr(label="Легенда", style="dotted")
            # Пример обычной вершины
            legend.node("legend_node", label="Обычная вершина (id)", shape="circle")
            # Пример терминальной вершины
            legend.node("legend_terminal", label="Терминальная вершина (id)", shape="circle", style="filled",
                        fillcolor="lightblue")
            # Пример перехода
            legend.edge("legend_node", "legend_terminal", label="Переход")
            # Пример суффиксной ссылки
            legend.edge("legend_terminal", "legend_node", style="dashed", color="red", label="Суффиксная ссылка")

        # Сохранение графа
        dot.render(file_name, format="png", cleanup=True, view=True)
        print(f"Граф сохранен в файл {file_name}.png")

    def print_bor_structure(self) -> None:
        """
        Печатает структуру бора.
        :return: None
        """
        print("\nСтруктура бора:")
        for v in self.vertices:
            parent_id = v.parent.id if v.parent else "None"
            pchar = v.pchar if v.pchar else ''
            transitions = []
            for idx, next_v in enumerate(v.next):
                if next_v is not None:
                    char = _char(idx)
                    transitions.append(f"'{char}': {next_v.id}")
            trans_str = ', '.join(transitions) if transitions else 'нет'
            term_info = f", терминальная (шаблоны: {v.pattern_numbers})" if v.is_terminal else ""
            print(f"Вершина {v.id}: родитель {parent_id}, символ '{pchar}'{term_info}, переходы: {trans_str}")

    def print_automaton_structure(self) -> None:
        """
        Печатает структуру автомата (суффиксные ссылки и переходы).
        :return: None
        """
        print("\nСтруктура автомата (суффиксные ссылки и переходы):")
        for v in self.vertices:
            suff_id = v.sufflink.id if v.sufflink else "None"
            go_trans = []
            for idx, go_v in enumerate(v.go):
                if go_v is not None:
                    char = _char(idx)
                    go_trans.append(f"'{char}': {go_v.id}")
            go_str = ', '.join(go_trans) if go_trans else 'нет'
            print(f"Вершина {v.id}: суффиксная ссылка -> {suff_id}, переходы go: {go_str}")
