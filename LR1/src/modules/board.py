"""
This module contains the class Board.
"""
from modules.square import Square


class Board:
    """
    This class represents the board.
    """

    def __init__(self, size: int) -> None:
        """
        This function initializes the board.
        :param size:
        """
        self.__size: int = size
        self.__board: list[list[int]] = [[0 for _ in range(size)] for _ in range(size)]
        self.__square_list: list[list[int, int, int]] = []
        self.__count_square: int = 0

    @property
    def size(self) -> int:
        """
        This function returns the size of the board.
        :return:
        """
        return self.__size

    @property
    def board(self) -> list[list[int]]:
        """
        This function returns the board.
        :return:
        """
        return self.__board

    @property
    def square_list(self) -> list[list[int, int, int]]:
        """
        This function returns the list of squares.
        :return:
        """
        return self.__square_list

    @property
    def count_square(self) -> int:
        """
        This function returns the number of squares.
        :return:
        """
        return self.__count_square

    def is_fill(self) -> bool:
        """
        This function checks if the board is full.
        :return:
        """
        for row in self.__board:
            if 0 in row:
                return False
        return True

    def get_empty_cell(self) -> tuple[int, int]:
        """
        This function returns the coordinates of the first empty cell.
        :return:
        """
        for row in range(len(self.__board)):
            for col in range(len(self.__board[row])):
                if self.__board[row][col] == 0:
                    return row, col
        return -1, -1

    def check_possible_square(self, x: int, y: int, side: int) -> bool:
        """
        This function checks if a square can be placed.
        :param x:
        :param y:
        :param side:
        :return:
        """
        if x + side > self.__size or y + side > self.__size or side <= 0 or x < 0 or y < 0:
            return False
        for i in range(x, x + side):
            for j in range(y, y + side):
                if self.__board[i][j] != 0:
                    return False
        return True

    def add_square(self, x: int, y: int, side: int) -> None:
        """
        This function adds a square to the board.
        :param x:
        :param y:
        :param side:
        :return:
        """
        square: Square = Square(side, x, y)
        for i in range(x, x + side):
            for j in range(y, y + side):
                self.__board[i][j] = self.__count_square + 1
        self.__square_list.append(square)
        self.__count_square += 1

    def place_squares_for_even_size(self) -> None:
        """
        This function places squares on the board for even size.
        :return:
        """
        self.add_square(0, 0, self.__size // 2)
        self.add_square(self.__size // 2, 0, self.__size // 2)
        self.add_square(0, self.__size // 2, self.__size // 2)
        self.add_square(self.__size // 2, self.__size // 2, self.__size // 2)

    def place_squares_for_prime_size(self) -> None:
        pass