#ifdef _WIN32
#include <windows.h>
#endif

#include "kmp.hpp"

int main() {
#ifdef _WIN32
    SetConsoleOutputCP(CP_UTF8);
#endif
    std::cout << "Задание №1 (KMP, найти все индексы)" << std::endl;
    std::string p, t;

    std::cin >> p >> t;

    if (const std::vector<int> result = kmp(t, p); result.empty()) std::cout << -1;
    else
        for (size_t i = 0; i < result.size(); ++i) {
            std::cout << result[i];
            if (i < result.size() - 1) std::cout << ",";
        }
    std::cout << std::endl;

    std::cout << "Задание №2 (Циклический сдвиг, найти первый индекс сдвига)" << std::endl;
    std::string a, b;
    std::cin >> a >> b;

    std::cout << find_cyclic_shift(a, b) << std::endl;
}
