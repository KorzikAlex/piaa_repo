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
        print(f"\nДобавление образца '{s}' (номер {pattern_num})")
        char: str
        for char in s:
            idx: int = _num(char)
            if v.next[idx] is None:
                print(f"\tСоздана вершина {self.size} для символа '{char}' (родитель {v.id})")
                self.vertices.append(Vertex(self.size, self.alpha, v, char))
                v.next[idx]: Vertex = self.last
            v: Vertex = v.next[idx]
        v.is_terminal = True
        print(f"\tВершина {v.id} помечена как терминальная для шаблонов {pattern_num}")
        v.pattern_numbers.append(pattern_num)

    def search(self, s: str) -> list[tuple[int, int]]:
        """
        Проверяет, есть ли строка в дереве.
        :param s: Строка для поиска.
        :return: Список кортежей (позиция, номер шаблона), где позиция - это индекс в строке s
        """
        res: list[tuple[int, int]] = []
        v: Vertex = self.root
        print(f"\nНачало поиска в строке: '{s}'")

        i: int
        char: str
        for i, char in enumerate(s):
            print(f"\nШаг {i + 1}: Символ '{char}' (позиция {i + 1})")
            v: Vertex = self.go(v, char)
            print(f"Текущая вершина: {v.id}")
            u: Vertex = v
            while u is not self.root:
                if u.is_terminal:
                    print(f"\tНайдена терминальная вершина {u.id} (шаблоны: {u.pattern_numbers})")
                    pid: int
                    for pid in u.pattern_numbers:
                        res.append((i, pid))
                u: Vertex = u.tlink if u.tlink is not None else self.root
                print(f"\tПереход по терминальной ссылке: {u.id}." if u != self.root else "Переход в корень.")
        print("\nПоиск завершен. Найдено совпадений:", len(res))
        return res

    def get_link(self, v: Vertex) -> Vertex:
        """
        Возвращает суффиксную ссылку для вершины v.
        :param v: Вершина, для которой нужно получить суффиксную ссылку.
        :return: Суффиксная ссылка для вершины v.
        """
        if v.sufflink is None:
            if self.root in (v, v.parent):
                print(f"\tСуффиксная ссылка вершины {v.id} установлена на корень")
                v.sufflink = self.root
            else:
                print(f"\tВычисление суффиксной ссылки для {v.id}: через родителя {v.parent.id} и символ '{v.pchar}'")
                v.sufflink = self.go(self.get_link(v.parent), v.pchar)
            print(f"\tВершина {v.id}: суффиксная ссылка -> {v.sufflink.id}")
            # Установка терминальной ссылки:
            v.tlink = v.sufflink if v.sufflink.is_terminal else v.sufflink.tlink
            # Вывод информации о терминальной ссылке
            if v.tlink:
                print(f"\tТерминальная ссылка вершины {v.id} установлена на {v.tlink.id}")
            else:
                print(f"\tТерминальная ссылка вершины {v.id} отсутствует")
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
                print(f"\tПрямой переход из {v.id} по '{char}' -> {v.next[idx].id}")
                v.go[idx]: Vertex = v.next[idx]
            elif v == self.root:
                print(f"\tКорневой переход из {v.id} по '{char}' -> корень")
                v.go[idx]: Vertex = self.root
            else:
                print(f"\tРекурсивный переход из {v.id} по '{char}' через суффиксную ссылку")
                v.go[idx]: Vertex = self.go(self.get_link(v), char)
        node: Vertex = v.go[idx]
        if node.sufflink is None:
            # Вызов “ленивого” get_link сам установит sufflink и tlink
            self.get_link(node)
        return node

    def precompute_sufflinks(self) -> None:
        """
        Предварительно вычисляет суффиксные ссылки для всех вершин.
        :return: None
        """
        v: Vertex
        for v in self.vertices[1:]:
            self.get_link(v)

    def visualize(self, file_name: str = "aho_corasick") -> None:
        """
        Создает графическое представление автомата Ахо-Корасик и сохраняет его в файл.
        :param file_name: Имя файла для сохранения графа (без расширения).
        :return: None
        """
        dot: Digraph = Digraph(comment="Aho-Corasick Automaton")
        dot.attr(rankdir="TB", fontsize="18", fontname="Arial")  # Вертикальное расположение графа

        with dot.subgraph(name="cluster_automaton") as automaton:
            # Настройка графа
            automaton.attr(label="Автомат Ахо-Корасик", style="dotted")  # Название, стиль обводки

            # Добавление вершин
            v: Vertex
            for v in self.vertices:
                if v == self.root:
                    label: str = "root" + f" ({v.id})"
                else:
                    label: str = (v.pchar if v.pchar is not None else '') + f" ({v.id})"
                if v.is_terminal:
                    automaton.node(str(v.id), label, shape="circle",
                                    style="filled", fillcolor="lightblue")
                else:
                    automaton.node(str(v.id), label, shape="circle")

            # Добавление переходов
            v: Vertex
            for v in self.vertices:
                next_v: Vertex
                for next_v in v.next:
                    if next_v is not None:
                        automaton.edge(str(v.id), str(next_v.id))

            # Добавление терминальных ссылок
            v: Vertex
            for v in self.vertices:
                if v.tlink is not None:
                    automaton.edge(str(v.id), str(v.tlink.id), style="dotted",
                                    color="blue", constraint="false")

            # Добавление суффиксных ссылок
            v: Vertex
            for v in self.vertices:
                if v.sufflink is not None and v.sufflink != v and v.sufflink != v.tlink:
                    automaton.edge(str(v.id), str(v.sufflink.id), style="dashed",
                                    color="red", constraint="false")

        with dot.subgraph(name="cluster_legend") as legend:
            # Добавление легенды
            legend.attr(label="Легенда", style="dotted", fontname="Arial", margin="20")
            # Пример обычной вершины
            legend.node("legend_node", label="Обычная\nвершина (id)", shape="circle",
                        width="0.5", height="0.3", fontsize="11")
            # Пример терминальной вершины
            legend.node("legend_terminal", label="Терминальная\nвершина (id)", shape="circle",
                        style="filled", fillcolor="lightblue", width="0.5",
                        height="0.3", fontsize="11")
            # Пример перехода
            legend.edge("legend_node", "legend_terminal", label="Переход", fontsize="11")
            # Пример суффиксной ссылки
            legend.edge("legend_terminal", "legend_node", style="dashed",
                        color="red", label="Суффиксная\nссылка", fontsize="11")
            # Пример терминальной ссылки
            legend.edge("legend_terminal", "legend_node", style="dotted",
                        color="blue", label="Терминальная\nссылка", fontsize="11")

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
            parent_id: int = v.parent.id if v.parent else -1
            pchar: str = v.pchar if v.pchar else ''
            transitions: list[str] = []
            idx: int
            next_v: Vertex
            for idx, next_v in enumerate(v.next):
                if next_v is not None:
                    char: str = _char(idx)
                    transitions.append(f"'{char}': {next_v.id}")
            trans_str: str = ', '.join(transitions) if transitions else 'нет'
            term_info: str = f", терминальная (шаблоны: {v.pattern_numbers})" if v.is_terminal else ""
            print(f"Вершина {v.id}: родитель {parent_id}, "
                    f"символ '{pchar}'{term_info}, переходы: {trans_str}")

    def print_automaton_structure(self) -> None:
        """
        Печатает структуру автомата (суффиксные ссылки и переходы).
        :return: None
        """
        print("\nСтруктура автомата (суффиксные ссылки и переходы):")
        for v in self.vertices:
            suff_id: int = v.sufflink.id if v.sufflink else -1
            tlink_id = v.tlink.id if v.tlink else -1
            go_trans: list[str] = []
            idx: int
            go_v: Vertex
            for idx, go_v in enumerate(v.go):
                if go_v is not None:
                    char: str = _char(idx)
                    go_trans.append(f"'{char}': {go_v.id}")
            go_str: str = ', '.join(go_trans) if go_trans else 'нет'
            print(f"Вершина {v.id}: суффиксная ссылка -> {suff_id}, "
                    f"терминальная ссылка -> {tlink_id}, переходы: {go_str}")
