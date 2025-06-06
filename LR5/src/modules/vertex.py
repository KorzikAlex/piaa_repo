#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Класс Vertex, представляющий вершину в автомате.
"""


class Vertex:
    """
    Класс, представляющий вершину в автомате.
    """

    def __init__(
            self, id_: int, alpha: int,
            parent: "Vertex" or None = None, pchar: str or None = None
    ) -> None:
        """
        Конструктор класса Vertex.
        :param id_: Идентификатор вершины.
        :param alpha: Количество символов в алфавите.
        :param parent: Родительская вершина.
        :param pchar: Символ, по которому произошел переход в эту вершину.
        """
        self.__id: int = id_  # Идентификатор вершины
        self.next: list[Vertex | None] = [None] * alpha  # Список переходов
        self.__is_terminal: bool = False  # Флаг, указывающий, заканчивается ли в этой вершине строка
        self.__parent: Vertex or None = parent  # Родительская вершина
        self.__pchar: str or None = pchar  # Символ, по которому произошел переход в эту вершину
        self.__sufflink: Vertex or None = None  # Суффиксная ссылка
        self.__tlink: Vertex or None = None  # Терминальная ссылка
        self.go: list[Vertex | None] = [None] * alpha  # Список переходов по символам
        self.pattern_numbers: list = []  # Номера шаблонов, заканчивающихся здесь

    @property
    def is_terminal(self) -> bool:
        """
        Возвращает True, если заканчивается в этой вершине образец.
        :return: True, если заканчивается, иначе False.
        """
        return self.__is_terminal

    @is_terminal.setter
    def is_terminal(self, value: bool) -> None:
        """
        Устанавливает флаг окончания образца.
        :param value: True, если заканчивается в этой вершине образец, иначе False.
        :return: None
        """
        self.__is_terminal = value

    @property
    def id(self) -> int:
        """
        Возвращает идентификатор вершины.
        :return: Идентификатор вершины.
        """
        return self.__id

    @property
    def sufflink(self) -> "Vertex" or None:
        """
        Возвращает суффиксную ссылку.
        :return: Суффиксная ссылка.
        """
        return self.__sufflink

    @sufflink.setter
    def sufflink(self, value: "Vertex" or None) -> None:
        """
        Устанавливает суффиксную ссылку.
        :param value: Суффиксная ссылка.
        :return: None
        """
        self.__sufflink = value

    @property
    def tlink(self) -> "Vertex" or None:
        """
        Возвращает терминальную ссылку.
        :return: Терминальная ссылка.
        """
        return self.__tlink

    @tlink.setter
    def tlink(self, value: "Vertex" or None) -> None:
        """
        Устанавливает терминальную ссылку.
        :param value: Терминальная ссылка.
        :return: None
        """
        self.__tlink = value

    @property
    def parent(self) -> "Vertex" or None:
        """
        Возвращает родительскую вершину.
        :return: Родительская вершина.
        """
        return self.__parent

    @property
    def pchar(self) -> str or None:
        """
        Возвращает символ, по которому произошел переход в эту вершину
        (символ родительской вершины).
        :return: Символ, по которому произошел переход в эту вершину.
        """
        return self.__pchar

    def __str__(self) -> str:
        parent_id: int | str = self.parent.id if self.parent else "None"
        sufflink_id: int | str = self.sufflink.id if self.sufflink else "None"
        tlink_id: int | str = self.tlink.id if self.tlink else "None"
        next_ids: list[tuple[int, int]] = [(i, v.id) for i, v in enumerate(self.next) if v is not None]
        go_ids: list[tuple[int, int]] = [(i, v.id) for i, v in enumerate(self.go) if v is not None]
        return (f"Vertex(id={self.id}, pchar='{self.pchar}', parent={parent_id}, "
                f"is_terminal={self.is_terminal}, pattern_numbers={self.pattern_numbers}, "
                f"sufflink={sufflink_id}, tlink={tlink_id}, next={next_ids}, go={go_ids})")
