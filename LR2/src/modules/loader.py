#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Модуль для загрузки и сохранения матрицы весов
"""
import random


def generate_mx(n: int, symmetric: bool = True, max_weight: int = 100) -> list[list[int]]:
    """
    Функция для генерации матрицы весов.
    :param symmetric: Если True, то матрица будет симметричной
    :param n: Размерность матрицы
    :param max_weight: Максимальный вес ребра
    :return: list[list[int]] Матрица весов
    """
    mx: list[list[int]] = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            w: int = random.randint(1, max_weight)
            mx[i][j]: int = w
            mx[j][i]: int = w if symmetric else random.randint(1, max_weight)
    return mx


def load_mx(file_name: str) -> tuple[int, list[list[int]]]:
    """
    Функция для загрузки файла.
    :param file_name: Имя файла
    :return: list[str] | None Список строк из файла
    """
    with open(file=file_name, mode="rt", encoding="UTF-8") as file:
        n: int = int(file.readline().strip())
        return n, [[int(i) for i in line.strip().split()] for line in file.readlines()]


def write_mx(file_name: str, weight_matrix: list[list[int]]) -> None:
    """
    Функция для записи в файл.
    :param weight_matrix: Матрица весов
    :param file_name: Имя файла
    :return: None
    """
    try:
        with open(file=file_name, mode="wt", encoding="UTF-8") as file:
            file.write(f"{len(weight_matrix)}\n")
            for row in weight_matrix:
                file.write(" ".join(map(str, row)) + "\n")
            return None
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return None
    except ValueError:
        print("Некорректный формат матрицы.")
        return None
    except Exception as e:
        print("Ошибка:", e)
        return None
