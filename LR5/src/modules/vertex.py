"""
Класс, представляющий вершину в автомате.
"""

class Vertex:
    """
    Класс, представляющий вершину в автомате.
    """
    def __init__(self, id: int, alpha, parent, pchar) -> None:
        """
        Конструктор класса Vertex.
        :param id:
        :param alpha:
        :param parent:
        :param pchar:
        """
        self.id = id # Идентификатор вершины
        self.next = [None] * alpha # Список переходов
        self.is_terminal = False # Флаг, указывающий, заканчивается ли в этой вершине строка
        self.parent = parent # Родительская вершина
        self.pchar = pchar # Символ, по которому произошел переход в эту вершину
        self.sufflink = None # Суффиксная ссылка
        self.go = [None] * alpha # Список переходов по символам
