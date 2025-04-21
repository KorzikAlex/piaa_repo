"""
Главный файл программы.

Вариант 2.
Подсчитать количество вершин в автомате;
Вывести список найденных образцов,
имеющих пересечения с другими найденными образцами в строке поиска.
"""
from modules.trie import Trie


def main() -> None:
    """
    Главная функция программы.
    :return: None
    """
    ALPHA = 5
    ALPHABET = ('A', 'C', 'G', 'T', 'N')

    print("Задание #1: Нахождение всех образцов в тексте")
    text: str = input().strip()
    n: int = int(input())
    patterns: list[str] = []
    t: Trie = Trie(ALPHA)
    for _ in range(n):
        pattern = input().strip()
        patterns.append(pattern)
        t.add(pattern)

    # print("Задание #2: Решение задачи точного поиска одного образца с джокером")
    # text: str = input().strip()
    # pattern: str = input().strip()
    # wildcard: str = input().strip()


if __name__ == '__main__':
    main()
