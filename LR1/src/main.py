"""
This is the main file of the project.

Вар. 2и. Итеративный бэктрекинг. Исследование времени выполнения от
размера квадрата.
"""
import timeit

from modules.board import Board

from modules.backtracking import backtracking_algorithm

def time_check() -> None:
    """
    This function checks the execution time of the backtracking algorithm for different board sizes.
    :return:
    """
    n_sizes = [2, 3, 4, 7, 9]
    for n in n_sizes:
        board = Board(n)
        exec_time = timeit.timeit(lambda: backtracking_algorithm(board), number=1)
        print(f"Execution time for board size {n}: {exec_time:.6f} seconds")


def main() -> None:
    """
    Main function of the project.
    :return:
    """
    n: int = int(input())
    board: Board = Board(n)
    result = backtracking_algorithm(board)
    print(result)


if __name__ == "__main__":
    main()
    # time_check()
