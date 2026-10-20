#include <vector>

void swap(std::vector<int>& v, int i, int j)
{
    int temp = v[i];
    v[i]= v[j];
    v[j] = temp;
}

int partition(std::vector<int>& v, int first, int last, int pivot)
{
    swap(v,pivot,last);
    int j = first;
    for (int i = first; i< last; i++)
    {
        if (v[i] <= v[last])
        {
            swap(v,i,j);
            j ++;
        }
    }
    swap(v,last,j);
    return j;
}

void quick_sort(std::vector<int>& v, int first, int last)
{
    if (first < last)
    {
        int pivot = first + (last-first)/2;
        pivot = partition(v,first,last,pivot);
        quick_sort(v,first,pivot -1);
        quick_sort(v,pivot+1,last);
    }
}


void quick_sort(std::vector<int>& v)
{
    quick_sort(v, 0, v.size()-1);
}

