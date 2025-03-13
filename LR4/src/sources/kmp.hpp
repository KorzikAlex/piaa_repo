#pragma once

#include <iostream>
#include <vector>

std::vector<int> prefix_func(const std::string &text);

std::vector<int> kmp(const std::string &text, const std::string &sub_text);

int find_cyclic_shift(const std::string &text, const std::string &sub_text);
