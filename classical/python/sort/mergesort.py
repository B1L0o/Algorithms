def helper(arr,left,mid,right):
    l_half = mid-left+1
    r_half = right-mid

    L = [0] * l_half
    R = [0] * r_half

    for i in range(l_half):
        L[i] = arr[left + i]
    for i in range(r_half):
        R[i] = arr[mid + 1 + i]

    i,j,k = 0,0,left

    while i < l_half and j < r_half:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j] 
            j += 1
        k += 1

    while i < l_half:
        arr[k] = L[i]
        i+=1
        k+=1

    while j < r_half:
        arr[k] = R[j]
        j+=1
        k+=1



def mergesort(arr,left,right):
    if left < right:
        mid = (left + right) // 2

        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        helper(arr,left,mid,right)

        global num
        print("AFTER ",num+1,"\tITERATIONS: \t", arr )
        num+=1

if __name__ == "__main__":
    num=0
    arr = [125,2 ,52, 512, 52,1 ,52 ,125 ,52,3 ,63, 6, 7,4 ]
    print("ARRAY BEFORE SORTING: \t\t", arr)
    mergesort(arr, 0, len(arr) - 1)