#include <vector>


int find_minimun(std::vector<int>& v, int left, int right, int actual)
{
    int pos = -1;
    while (left < right)
    {
        if (v[left] < actual)
        {
            pos = left; 
            actual = v[left];
        }
        left ++;
    }
    return pos;
}

void swap(std::vector<int>& v, int i, int j, int temp)
{
    temp = v[i];
    v[i] = v[j];
    v[j] = temp;
}

void insertion_sort(std::vector<int>& v)
{
    int n = v.size();
    int min_pos, temp;
    for (int i = 0; i < n-1; i++)
    {
        min_pos = find_minimun(v,i+1,n,v[i]);
        if (min_pos != -1)
        {
            swap(v,i,min_pos,temp);
        }
    }           
}

