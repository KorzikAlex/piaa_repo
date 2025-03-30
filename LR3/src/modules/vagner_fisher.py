"""
Модуль для вычисления алгоритма Вагнера-Фишера.
"""


def _wagner_fisher_step(i: int, j: int, s1: str, s2: str, matrix: list[list[int]],
                        rep_cost: int, ins_cost: int, del_cost: int, ins2_cost: int) -> int:
    """
    Вычисляет шаг алгоритма Вагнера-Фишера для двух строк s1 и s2.
    :param i:
    :param j:
    :param s1:
    :param s2:
    :param matrix:
    :param rep_cost:
    :param ins_cost:
    :param del_cost:
    :param ins2_cost:
    :return:
    """
    if i == 0 and j == 0:
        return 0
    if j == 0:
        return i * del_cost
    if i == 0:
        # При пустой строке s1 можно накапливать вставки.
        if j == 1:
            return matrix[0][0] + ins_cost
        # Выбираем минимальный вариант: либо единичная вставка, либо двойная вставка.
        return min(matrix[0][j - 1] + ins_cost, matrix[0][j - 2] + ins2_cost)

    # Замена или совпадение
    rep: int = matrix[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else rep_cost)
    ins: int = matrix[i][j - 1] + ins_cost
    dele: int = matrix[i - 1][j] + del_cost

    candidates: list[int] = [rep, ins, dele]
    if j >= 2:
        # Операция последовательной вставки двух символов
        candidates.append(matrix[i][j - 2] + ins2_cost)
    return min(candidates)


def calculate_edit_distance(s1: str, s2: str,
                            rep_cost: int = 1, ins_cost: int = 1,
                            del_cost: int = 1, ins2_cost: int = 1) -> int:
    """
    Вычисляет расстояние редактирования между строками s1 и s2
    с учётом операций: замены, вставки, удаления и
    последовательной вставки двух одинаковых символов.
    :param s1:
    :param s2:
    :param rep_cost:
    :param ins_cost:
    :param del_cost:
    :param ins2_cost:
    :return:
    """
    n, m = len(s1), len(s2)
    matrix: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            matrix[i][j] = _wagner_fisher_step(i, j, s1, s2, matrix,
                                               rep_cost, ins_cost,
                                               del_cost, ins2_cost)
    return matrix[n][m]


def compute_edit_sequence(s1: str, s2: str,
                          rep_cost: int = 1, ins_cost: int = 1,
                          del_cost: int = 1, ins2_cost: int = 1) -> str:
    """
    Вычисляет последовательность операций для преобразования строки s1 в s2
    с учётом дополнительных затрат при последовательной вставке двух символов.

    Обозначения:
        M – совпадение (match)
        R – замена (replacement)
        I – вставка одного символа
        D – удаление символа
        P – последовательная вставка двух одинаковых символов
    :param s1:
    :param s2:
    :param rep_cost:
    :param ins_cost:
    :param del_cost:
    :param ins2_cost:
    :return:
    """
    n, m = len(s1), len(s2)

    # Матрица для стоимости и для операций
    cost: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    back: list[list[str]] = [[''] * (m + 1) for _ in range(n + 1)]

    # Инициализация первого столбца (удаления)
    for i in range(1, n + 1):
        cost[i][0]: int = cost[i - 1][0] + del_cost
        back[i][0]: str = 'D'

    # Инициализация первой строки (вставки)
    if m >= 1:
        cost[0][1]: int = cost[0][0] + ins_cost
        back[0][1]: str = 'I'

    for j in range(2, m + 1):
        # Рассматриваем либо наращивание через единичную вставку, либо операцию двойной вставки
        candidate_single: int = cost[0][j - 1] + ins_cost
        candidate_double: int = cost[0][j - 2] + ins2_cost
        if candidate_double < candidate_single:
            cost[0][j]: int = candidate_double
            back[0][j]: str = 'P'
        else:
            cost[0][j]: int = candidate_single
            back[0][j]: str = 'I'

    # Заполнение матрицы динамического программирования
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Замена или совпадение
            if s1[i - 1] == s2[j - 1]:
                rep_val: int = cost[i - 1][j - 1]
                op_rep: str = 'M'
            else:
                rep_val: int = cost[i - 1][j - 1] + rep_cost
                op_rep: str = 'R'
            # Вставка одного символа
            ins_val: int = cost[i][j - 1] + ins_cost
            op_ins: str = 'I'
            # Удаление символа
            del_val: int = cost[i - 1][j] + del_cost
            op_del: str = 'D'

            best: int = rep_val
            best_op: str = op_rep

            if ins_val < best:
                best: int = ins_val
                best_op: str = op_ins
            if del_val < best:
                best: int = del_val
                best_op: str = op_del

            if j >= 2:
                # Последовательная вставка двух одинаковых символов
                double_ins_val: int = cost[i][j - 2] + ins2_cost
                if double_ins_val < best:
                    best: int = double_ins_val
                    best_op: str = 'P'

            cost[i][j]: int = best
            back[i][j]: str = best_op

    # Обратное отслеживание для восстановления последовательности операций
    i, j = n, m
    operations: list = []
    while i > 0 or j > 0:
        op: str = back[i][j]
        operations.append(op)
        if op in ('M', 'R'):
            i -= 1
            j -= 1
        elif op == 'I':
            j -= 1
        elif op == 'D':
            i -= 1
        elif op == 'P':
            j -= 2
    operations.reverse()
    return ''.join(operations)
