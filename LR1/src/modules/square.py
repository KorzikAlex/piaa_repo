"""
This module contains the class Square.
"""


class Square:
    """
    This class represents the square.
    """

    def __init__(self, side: int, x: int, y: int) -> None:
        """
        This function initializes the square.
        :param side:
        :param x:
        :param y:
        """
        self.__side: int = side
        self.__x: int = x
        self.__y: int = y

    @property
    def side(self) -> int:
        """
        This function returns the side of the square.
        :return:
        """
        return self.__side

    @property
    def x(self) -> int:
        """
        This function returns the x coordinate of the square.
        :return:
        """
        return self.__x

    @property
    def y(self) -> int:
        """
        This function returns the y coordinate of the square.
        :return:
        """
        return self.__y
