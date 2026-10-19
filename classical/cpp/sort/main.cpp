#include <vector>
#include <iostream>

#include "bubble_sort/bubble_sort.h"
#include "insertion_sort/insertion_sort.h"

int main()
{
    std::vector<int> v = {12, 4, 232, 52, 120 ,52 ,63 , 7 ,2 ,46, 5};
    //bubble_sort(v);
    insertion_sort(v);

    for (int e : v)
    {
        std::cout << e << " ";
    }
    std::cout << '\n';
}

