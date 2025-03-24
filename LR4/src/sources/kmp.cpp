/**
 * @file kmp.cpp
 * @author Korzik
 * @brief Реализация алгоритма Кнута-Морриса-Пратта и поиска циклического сдвига
 */
#include "kmp.hpp"

std::vector<int> prefix_func(const std::string &text) {
    std::vector pi(text.size(), 0);
    int j = 0;

    std::cout << "Для первого символа text[0] = '" << text[0] << "' pi[0] = 0" << std::endl;
    for (int i = 1; i < text.size(); ++i) {
        std::cout << "\nОбработка символа text[" << i << "] = '" << text[i] << "'" << std::endl;
        j = pi[i - 1];
        std::cout << "\tИзначально j = pi[" << (i - 1) << "] = " << j << std::endl;

        while (j > 0 && text[i] != text[j]) {
            std::cout << "\ttext[" << i << "] != text[" << j << "] (" << text[i] << " != " << text[j] << "), j = pi["
                    << (j - 1) << "] = " << pi[j - 1] << std::endl;
            j = pi[j - 1];
        }

        if (text[i] == text[j]) {
            std::cout << "\tСовпадение: text[" << i << "] == text[" << j << "] (" << text[i] << "), увеличиваем j до "
                    << (j + 1) << std::endl;
            j++;
        } else std::cout << "\tСовпадений нет, j остается 0" << std::endl;


        pi[i] = j;
        std::cout << "\tУстановлен pi[" << i << "] = " << j << std::endl;
    }

    std::cout << "\nИтоговая префикс-функция: ";
    for (size_t idx = 0; idx < pi.size(); ++idx) {
        std::cout << pi[idx];
        if (idx != pi.size() - 1) std::cout << ", ";
    }
    std::cout << std::endl << std::endl;

    return pi;
}

std::vector<int> kmp(const std::string &text, const std::string &sub_text) {
    std::vector<int> res_indexes;
    std::cout << "Запуск KMP для поиска \"" << sub_text << "\" в \"" << text << "\"" << std::endl << std::endl;
    int j = 0;
    std::cout << "Этап 1: Вычисление префикс-функции для подстроки" << std::endl;
    const std::vector<int> pi = prefix_func(sub_text);

    std::cout << "Этап 2: Поиск подстроки в тексте" << std::endl;
    for (int i = 0; i < text.size(); ++i) {
        std::cout << "\nТекущий символ текста: text[" << i << "] = '" << text[i] << "'" << std::endl;
        while (j > 0 && text[i] != sub_text[j]) {
            std::cout << "\tНесовпадение: text[" << i << "] != sub_text[" << j << "] (" << text[i] << " != "
                    << sub_text[j] << "), j = pi[" << (j - 1) << "] = " << pi[j - 1] << std::endl;
            j = pi[j - 1];
        }
        if (text[i] == sub_text[j]) {
            std::cout << "\tСовпадение: text[" << i << "] == sub_text[" << j << "] ("
                    << text[i] << "), увеличиваем j до " << (j + 1) << std::endl;
            j++;
        } else std::cout << "\tСовпадений нет, j остается " << j << std::endl;

        if (j >= sub_text.size()) {
            std::cout << "!!! Найдено полное вхождение на позиции " << i - j + 1 << " !!!" << std::endl;
            res_indexes.push_back(i - j + 1);
            j = pi[j - 1];
            std::cout << "\tСброс j = pi[" << (sub_text.size() - 1) << "] = " << j << std::endl;
        }
    }
    return res_indexes;
}

int index_cyclic_shift(const std::string &text, const std::string &sub_text) {
    std::cout << "Поиск циклического сдвига между \"" << text << "\" и \"" << sub_text << "\"" << std::endl;
    if (text.size() != sub_text.size()) {
        std::cerr << "Ошибка: длины строк отличаются (" << text.size() << " vs " << sub_text.size() << ")" << std::endl;
        return -1;
    }
    int j = 0;
    std::cout << "\nЭтап 1: Вычисление префикс-функции для подстроки" << std::endl;
    const std::vector<int> pi = prefix_func(sub_text);

    std::cout << "Этап 2: Поиск циклического сдвига" << std::endl;
    for (int i = 0; i < text.size() * 2; ++i) {
        const int mod_idx = i % text.size();
        std::cout << "\nШаг " << i << ": text[" << mod_idx << "] = '" << text[mod_idx]
                << "', sub_text[" << j << "] = '" << sub_text[j] << "'" << std::endl;
        while (j > 0 && text[mod_idx] != sub_text[j]) {
            std::cout << "\tНесовпадение: text[" << mod_idx << "] != sub_text[" << j << "] (" << text[mod_idx] << " != "
                    << sub_text[j] << "), j = pi[" << (j - 1) << "] = " << pi[j - 1] << std::endl;
            j = pi[j - 1];
        }
        if (text[mod_idx] == sub_text[j]) {
            std::cout << "\tСовпадение: text[" << mod_idx << "] == sub_text[" << j << "] ("
                    << text[mod_idx] << "), увеличиваем j до " << (j + 1) << std::endl;
            j++;
        } else std::cout << "\tСовпадений нет, j остается " << j << std::endl;

        if (j == sub_text.size()) {
            std::cout << "!!! Найден циклический сдвиг: " << i - j + 1 << " !!!" << std::endl;
            return i - j + 1;
        }
    }
    std::cout << "\nЦиклический сдвиг не найден" << std::endl;
    return -1;
}
