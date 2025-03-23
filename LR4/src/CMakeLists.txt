cmake_minimum_required(VERSION 3.20) # проверка версии CMake

project(kmp) # название проекта

set(CMAKE_CXX_STANDARD 20) # стандарт C++

add_executable(kmp sources/main.cpp sources/kmp.cpp) # исполняемый файл