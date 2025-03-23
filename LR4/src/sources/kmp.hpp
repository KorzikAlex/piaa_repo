/**
 * @file kmp.hpp
 * @author Korzik
 * @brief Заголовочный файл для kmp.cpp
 */
#pragma once


#include <iostream>
#include <vector>

/**
 * @brief Функция для вычисления префикс-функции
 * @param text Строка для вычисления префикс-функции
 * @return Значения префикс-функции (векторная форма)
 */
std::vector<int> prefix_func(const std::string &text);

/**
 * @brief Функция для поиска подстроки в строке
 * @param text Строка для поиска подстроки
 * @param sub_text Подстрока для поиска
 * @return Вектор индексов, где найдена подстрока
 */
std::vector<int> kmp(const std::string &text, const std::string &sub_text);

/**
 * @brief Функция для поиска циклического сдвига
 * @param text Строка для поиска циклического сдвига
 * @param sub_text Подстрока для поиска
 * @return Индекс сдвига
 */
int find_cyclic_shift(const std::string &text, const std::string &sub_text);
