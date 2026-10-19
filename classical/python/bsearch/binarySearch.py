def bsearch(arr,x):
    L = 0
    R= len(arr)-1

    while L <= R:
        M = (L+R)//2

        if arr[M] == x:
            return M
        
        if arr[M] < x:
            L = M+1

        else:
            R = M-1

    return -1