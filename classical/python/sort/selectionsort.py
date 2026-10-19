def selection_sort(arr):
    n=len(arr)
    for i in range(n-1):
        min_val=arr[i]
        pos=i
        for j in range(i+1,n):
            if arr[j] < min_val:
                min_val=arr[j]
                pos=j
        arr[i],arr[pos] = arr[pos],arr[i]
        print("AFTER ",i+1,"\tITERATIONS: \t", arr )

if __name__ == "__main__":
    arr = [125,2 ,52, 512, 52,1 ,52 ,125 ,52,3 ,63, 6, 7,4 ]
    print("ARRAY BEFORE SORTING: \t\t", arr)
    selection_sort(arr)