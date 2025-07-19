def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        m=arr[i]
        pos=i
        for j in range(i+1,n):
            if arr[j] < m:
                m=arr[j]
                pos=j
        arr[i],arr[pos] = arr[pos],arr[i]