/**
 * @file main.cpp
 * @author Korzik
 * @brief Главный файл программы
 */
#ifdef _WIN32
#include <windows.h>
#endif

#include "kmp.hpp"

/**
 * @brief Главная функция программы, содержит два задания (KMP и циклический сдвиг)
 * @return 0
 */
int main() {
#ifdef _WIN32
    SetConsoleCP(CP_UTF8);
    SetConsoleOutputCP(CP_UTF8);
#endif
    std::cout << "Задание №1 (KMP, найти все индексы)" << std::endl;
    std::string p, t; // Подстрока и строка

    std::cin >> p >> t; // Вводим подстроку и строку

    if (const std::vector<int> result = kmp(t, p); !result.empty()) {
        std::cout << "Кол-во найденных вхождений: " << result.size() << std::endl; // Выводим кол-во вхождений
        std::cout << "Индексы: ";
        for (size_t i = 0; i < result.size(); ++i) {
            // Проходим по всем индексам
            std::cout << result[i]; // Выводим результат
            if (i < result.size() - 1) std::cout << ","; // Если не последний элемент, то выводим запятую
        }
    }
    else std::cout << "Нет вхождений " << -1; // Если нет совпадений, то выводим -1

    std::cout << std::endl << std::endl;

    std::cout << "Задание №2 (Циклический сдвиг, найти первый индекс сдвига)" << std::endl;
    std::string a, b; // Строки
    std::cin >> a >> b; // Вводим строки

    std::cout << "Индекс сдвига строки: " << find_cyclic_shift(a, b) << std::endl; // Выводим результат
}
