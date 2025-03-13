cmake_minimum_required(VERSION 3.20)

project(kmp)

set(CMAKE_CXX_STANDARD 20)

add_executable(kmp sources/main.cpp sources/kmp.cpp)