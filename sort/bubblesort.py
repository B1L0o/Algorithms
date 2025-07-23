import random

def bubble_sort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
        print("AFTER ",i+1,"\tITERATIONS: \t", arr )

if __name__ == "__main__":
    arr = [random.randint(10, 500) for _ in range(500)]
    print("ARRAY BEFORE SORTING: \t\t", arr)
    bubble_sort(arr)