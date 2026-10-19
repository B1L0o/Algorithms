#include <vector>

void bubble_sort(std::vector<int>& v)
{
    int n = v.size();
    int temp;
    for (int i = 0; i < n-1; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if (v[i] > v[j])
            {
                temp  = v[i];
                v[i] = v[j];
                v[j] = temp;
            }
        }
    }           
}

