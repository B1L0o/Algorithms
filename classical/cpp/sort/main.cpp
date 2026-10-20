#include <vector>
#include <iostream>

#include "bubble_sort/bubble_sort.h"
#include "selection_sort/selection_sort.h"
#include "quick_sort/quick_sort.h"

int main()
{
    std::vector<int> v = {12, 4, 232, 52, 120 ,52 ,63 , 7 ,2 ,46, 5};
    //bubble_sort(v);
    //selection_sort(v);
    quick_sort(v);

    for (int e : v)
    {
        std::cout << e << " ";
    }
    std::cout << '\n';
}

