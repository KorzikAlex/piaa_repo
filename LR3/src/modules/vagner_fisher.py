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
    print(f"--- Вычисление ячейки ({i}, {j}) ---")
    if i == 0 and j == 0:
        print("Начальная ячейка (0, 0), значение 0.")
        return 0
    if j == 0:
        val: int = i * del_cost
        print(f"j=0: удаление {i} символов. Значение = {val}.")
        return val
    if i == 0:
        if j == 1:
            val: int = matrix[0][0] + ins_cost
            print(f"i=0, j=1: единичная вставка. Значение = {val} (0 + {ins_cost}).")
            return val
        val1: int = matrix[0][j - 1] + ins_cost
        val2: int = matrix[0][j - 2] + ins2_cost
        val: int = min(val1, val2)
        print(f"i=0, j={j}: варианты {val1} (одиночная вставка) "
              f"и {val2} (двойная вставка). "
              f"Минимум: {val}.")
        return val

    # Замена или совпадение
    rep: int = matrix[i - 1][j - 1] + (0 if s1[i - 1] == s2[j - 1] else rep_cost)
    ins: int = matrix[i][j - 1] + ins_cost
    dele: int = matrix[i - 1][j] + del_cost

    candidates: list[int] = [rep, ins, dele]
    if j >= 2:
        ins2_val = matrix[i][j - 2] + ins2_cost
        print(f"Двойная вставка: {ins2_val} (база {matrix[i][j - 2]} + {ins2_cost})")
        candidates.append(ins2_val)
    else:
        print("Двойная вставка недоступна (j < 2)")
    print(f"Кандидаты для ячейки ({i}, {j}): {candidates}. "
          f"Минимальное значение: {min(candidates)}.")
    return min(candidates)


def calculate_edit_distance(s1: str, s2: str,
                            rep_cost: int = 1, ins_cost: int = 1,
                            del_cost: int = 1, ins2_cost: int = 2) -> int:
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
            print(f"Текущее значение матрицы[{i}][{j}] = {matrix[i][j]}")
        print(f"\nСостояние матрицы после строки i={i}:")
        for row in matrix[:i + 1]:
            print(' '.join(map(str, row)))
        print("-" * 50 + "\n")
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

    cost: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    back: list[list[str]] = [[''] * (m + 1) for _ in range(n + 1)]

    print("\n" + "=" * 50)
    print("Инициализация первого столбца (операции удаления):")
    for i in range(1, n + 1):
        cost[i][0]: int = cost[i - 1][0] + del_cost
        back[i][0]: str = 'D'
        print(f"\ti={i}, j=0 → УДАЛЕНИЕ (D). cost[{i}][0] = {cost[i][0]} "
              f"(предыдущее {cost[i-1][0]} + {del_cost})")

    print("\n" + "=" * 50)
    print("Инициализация первой строки (операции вставки):")
    if m >= 1:
        cost[0][1]: int = cost[0][0] + ins_cost
        back[0][1]: str = 'I'
        print(f"\ti=0, j=1 → ВСТАВКА (I). cost[0][1] = {cost[0][1]} (0 + {ins_cost})")

    for j in range(2, m + 1):
        candidate_single: int = cost[0][j - 1] + ins_cost
        candidate_double: int = cost[0][j - 2] + ins2_cost
        print(f"\n  i=0, j={j}:")
        print(f"\tВариант 1: одиночная вставка → {candidate_single} "
              f"(cost[0][{j - 1}]={cost[0][j - 1]} + {ins_cost})")
        print(f"\tВариант 2: двойная вставка → {candidate_double} "
              f"(cost[0][{j - 2}]={cost[0][j - 2]} + {ins2_cost})")
        if candidate_double < candidate_single:
            cost[0][j]: int = candidate_double
            back[0][j]: str = 'P'
            print("\tВыбрана ДВОЙНАЯ ВСТАВКА (P)")
        else:
            cost[0][j]: int = candidate_single
            back[0][j]: str = 'I'
            print("\tВыбрана ОДИНОЧНАЯ ВСТАВКА (I)")
        print(f"\tcost[0][{j}] = {cost[0][j]}, back[0][{j}] = '{back[0][j]}'")

    print("\n" + "=" * 50)
    print("Заполнение основной матрицы:")
    for i in range(1, n + 1):
        print(f"\nОбработка строки i={i}:")
        for j in range(1, m + 1):
            print(f"\n--- Ячейка ({i}, {j}) ---")
            print(f"\tСимволы: s1[{i - 1}] = '{s1[i - 1]}', s2[{j - 1}] = '{s2[j - 1]}'")
            if s1[i - 1] == s2[j - 1]:
                rep_val: int = cost[i - 1][j - 1]
                op_rep: str = 'M'
                print(f"\tСОВПАДЕНИЕ (M): cost = {rep_val}")
            else:
                rep_val: int = cost[i - 1][j - 1] + rep_cost
                op_rep: str = 'R'
                print(f"\tЗАМЕНА (R): cost = {cost[i - 1][j - 1]} + {rep_cost} = {rep_val}")

            ins_val: int = cost[i][j - 1] + ins_cost
            op_ins: str = 'I'
            print(f"\tВСТАВКА (I): cost = {cost[i][j - 1]} + {ins_cost} = {ins_val}")

            del_val: int = cost[i - 1][j] + del_cost
            op_del: str = 'D'
            print(f"\tУДАЛЕНИЕ (D): cost = {cost[i - 1][j]} + {del_cost} = {del_val}")

            best: int = rep_val
            best_op: str = op_rep

            if ins_val < best:
                best: int = ins_val
                best_op: str = op_ins
            if del_val < best:
                best: int = del_val
                best_op: str = op_del

            if j >= 2:
                double_ins_val: int = cost[i][j - 2] + ins2_cost
                print(f"\tДВОЙНАЯ ВСТАВКА (P): cost = {cost[i][j - 2]} + {ins2_cost} = {double_ins_val}")
                if double_ins_val < best:
                    best: int = double_ins_val
                    best_op: str = 'P'

            cost[i][j]: int = best
            back[i][j]: str = best_op
            print(f"  Выбранная операция: '{best_op}' → cost[{i}][{j}] = {best}")

    print("\n" + "=" * 50)
    print("Восстановление последовательности операций:")
    i, j = n, m
    operations: list = []
    while i > 0 or j > 0:
        op: str = back[i][j]
        operations.append(op)
        print(f"  Позиция ({i}, {j}): операция '{op}'")
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
