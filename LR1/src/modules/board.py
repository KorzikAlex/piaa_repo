"""
Этот модуль содержит класс Board, который представляет доску n*n размером.
"""


class Board:
    """
    Этот класс представляет доску n*n размером.
    """

    def __init__(self, size: int) -> None:
        """
        Эта функция инициализирует доску.
        :param size:
        """
        self.__size: int = size
        self.__board: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
        self.__square_list: list[list[int]] = []
        self.__count_square: int = 0

    @property
    def size(self) -> int:
        """
        Эта функция возвращает размер доски.
        :return:
        """
        return self.__size

    @property
    def board(self) -> list[list[int]]:
        """
        Эта функция возвращает доску.
        :return:
        """
        return self.__board

    @property
    def square_list(self) -> list[list[int]]:
        """
        Эта функция возвращает список квадратов.
        :return:
        """
        return self.__square_list

    @property
    def count_square(self) -> int:
        """
        Эта функция возвращает количество квадратов.
        :return:
        """
        return self.__count_square

    def __deepcopy__(self, memodict: dict = None) -> 'Board':
        """
        Эта функция создает копию объекта. (глубокое копирование)
        :param memodict:
        :return:
        """
        new_board: Board = Board(self.__size)
        new_board.__board: list[list[int]] = [row[:] for row in self.__board]
        new_board.__square_list: list[list[int]] = [square[:] for square in self.__square_list]
        new_board.__count_square: int = self.__count_square
        return new_board

    def is_fill(self) -> bool:
        """
        Эта функция проверяет, заполнена ли доска.
        :return:
        """
        row: list[int]
        for row in self.__board:
            if 0 in row:
                return False
        return True

    def get_empty_cell(self) -> tuple[int, int]:
        """
        Эта функция возвращает пустую ячейку.
        :return:
        """
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                if self.__board[row][col] == 0:
                    return row, col
        return -1, -1

    def check_possible_square(self, x: int, y: int, side: int) -> bool:
        """
        Эта функция проверяет, можно ли добавить квадрат на доску.
        :param x:
        :param y:
        :param side:
        :return:
        """
        if (x + side > self.__size) or (y + side > self.__size) or side <= 0 or x < 0 or y < 0:
            return False
        for i in range(x, x + side):
            for j in range(y, y + side):
                if self.__board[i][j] != 0:
                    return False
        return True

    def add_square(self, x: int, y: int, side: int) -> None:
        """
        Эта функция добавляет квадрат на доску.
        :param x:
        :param y:
        :param side:
        :return:
        """
        for i in range(x, x + side):
            for j in range(y, y + side):
                self.__board[i][j] = self.__count_square + 1
        self.__square_list.append([x, y, side])
        self.__count_square += 1

    def place_squares_for_even_size(self) -> None:
        """
        Эта функция размещает квадраты на доске для четного размера.
        :return:
        """
        self.add_square(0, 0, self.__size // 2)
        self.add_square(self.__size // 2, 0, self.__size // 2)
        self.add_square(0, self.__size // 2, self.__size // 2)
        self.add_square(self.__size // 2, self.__size // 2, self.__size // 2)

    def place_squares_for_prime_size(self) -> None:
        """
        Эта функция размещает квадраты на доске для простого размера.
        :return:
        """
        self.add_square(0, 0, self.__size // 2 + 1)
        self.add_square(0, self.__size // 2 + 1, self.__size // 2)
        self.add_square(self.__size // 2 + 1, 0, self.__size // 2)
