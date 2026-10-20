cmake_minimum_required(VERSION 3.16)
project(sort CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(main
    main.cpp
    bubble_sort/bubble_sort.cpp
    selection_sort/selection_sort.cpp
    quick_sort/quick_sort.cpp
)