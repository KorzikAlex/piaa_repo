"""
Модуль для вычисления алгоритма Вагнера-Фишера.
"""


def _wagner_fisher_step(i: int, j: int, s1: str, s2: str, matrix: list[list[int]],
                        rep_cost: int, ins_cost: int, del_cost: int) -> int:
    """
    Функция для вычисления шага алгоритма Вагнера-Фишера.
    :param i:
    :param j:
    :param s1:
    :param s2:
    :param matrix:
    :param rep_cost:
    :param ins_cost:
    :param del_cost:
    :return:
    """
    if i == 0 and j == 0:
        return 0
    if j == 0:
        return i * del_cost
    if i == 0:
        return j * ins_cost

    replace: int = matrix[i - 1][j - 1] + (rep_cost if s1[i - 1] != s2[j - 1] else 0)
    insert: int = matrix[i][j - 1] + ins_cost
    delete: int = matrix[i - 1][j] + del_cost

    return min(insert, delete, replace)


def calculate_edit_distance(s1: str, s2: str,
                            rep_cost: int = 1, ins_cost: int = 1, del_cost: int = 1) -> int:
    """
    Функция для вычисления алгоритма Вагнера-Фишера.
    :param s1:
    :param s2:
    :param rep_cost:
    :param ins_cost:
    :param del_cost:
    :return:
    """
    n, m = len(s1), len(s2)
    matrix: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            matrix[i][j]: int = _wagner_fisher_step(i, j, s1, s2, matrix, rep_cost, ins_cost, del_cost)
    return matrix[n][m]


def compute_edit_sequence(s1: str, s2: str, rep_cost: int, ins_cost: int, del_cost: int) -> str:
    """
    Функция для вычисления последовательности операций алгоритма Вагнера-Фишера.
    :param s1:
    :param s2:
    :param rep_cost:
    :param ins_cost:
    :param del_cost:
    :return:
    """
    n, m = len(s1), len(s2)

    # Матрица для стоимости
    cost = [[0] * (m + 1) for _ in range(n + 1)]
    # Матрица для обратных указателей (операций)
    back = [[''] * (m + 1) for _ in range(n + 1)]

    # Инициализация первой строки и первого столбца
    for i in range(1, n + 1):
        cost[i][0] = cost[i - 1][0] + del_cost
        back[i][0] = 'D'  # Удаление (от верхней ячейки)
    for j in range(1, m + 1):
        cost[0][j] = cost[0][j - 1] + ins_cost
        back[0][j] = 'I'  # Вставка (от левой ячейки)

    # Заполнение матрицы динамического программирования
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Проверяем, совпадают ли символы
            if s1[i - 1] == s2[j - 1]:
                replace_cost = cost[i - 1][j - 1]  # Матч (без затрат)
            else:
                replace_cost = cost[i - 1][j - 1] + rep_cost  # Замена
            insert_cost = cost[i][j - 1] + ins_cost
            delete_cost = cost[i - 1][j] + del_cost

            # Определяем минимальную стоимость и сохраняем операцию
            min_cost = replace_cost
            op = 'M' if s1[i - 1] == s2[j - 1] else 'R'
            if insert_cost < min_cost:
                min_cost = insert_cost
                op = 'I'
            if delete_cost < min_cost:
                min_cost = delete_cost
                op = 'D'
            cost[i][j] = min_cost
            back[i][j] = op

    # Обратное отслеживание (backtracking) для восстановления последовательности операций
    i, j = n, m
    operations = []
    while i > 0 or j > 0:
        op = back[i][j]
        operations.append(op)
        if op in ('M', 'R'):
            i -= 1
            j -= 1
        elif op == 'I':
            j -= 1
        elif op == 'D':
            i -= 1

    operations.reverse()  # Получаем правильный порядок операций
    return ''.join(operations)
