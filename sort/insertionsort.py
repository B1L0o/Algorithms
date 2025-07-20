def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        j = i-1
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            j-=1
    print("AFTER ",i+1,"\tITERATIONS: \t", arr )

if __name__ == "__main__":
    arr = [125,2 ,52, 512, 52,1 ,52 ,125 ,52,3 ,63, 6, 7,4 ]
    print("ARRAY BEFORE SORTING: \t\t", arr)
    insertion_sort(arr)