/**
 * @file kmp.cpp
 *
 */
#include "kmp.hpp"

std::vector<int> prefix_func(const std::string &text) {
    std::vector pi(text.size(), 0);
    int j = 0;

    for (int i = 1; i < text.size(); ++i) {
        j = pi[i - 1];
        while (j > 0 && text[i] != text[j]) j = pi[j - 1];
        if (text[i] == text[j]) j++;
        pi[i] = j;
    }
    return pi;
}

std::vector<int> kmp(const std::string &text, const std::string &sub_text) {
    std::vector<int> res_indexes;

    int j = 0;
    const std::vector<int> pi = prefix_func(sub_text);

    for (int i = 0; i < text.size(); ++i) {
        while (j > 0 && text[i] != sub_text[j]) j = pi[j - 1];
        if (text[i] == sub_text[j]) j++;
        if (j >= sub_text.size()) {
            res_indexes.push_back(i - j + 1);
            j = pi[j - 1];
        }
    }
    return res_indexes;
}

int find_cyclic_shift(const std::string &text, const std::string &sub_text) {
    if (text.size() != sub_text.size()) return -1;

    int j = 0;
    const std::vector<int> pi = prefix_func(sub_text);

    for (int i = 0; i < text.size() * 2; ++i) {
        while (j > 0 && text[i % text.size()] != sub_text[j]) j = pi[j - 1];
        if (text[i % text.size()] == sub_text[j]) j++;
        if (j == sub_text.size()) return i - j + 1;
    }
    return -1;
}
