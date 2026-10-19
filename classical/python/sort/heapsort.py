import heapq

def heapsort(arr):
    n=len(arr)
    pq = []

    for element in arr:
        heapq.heappush(pq,element)

    for i in range(n):
        arr[i] = heapq.heappop(pq)
        print("AFTER ",i+1,"\tITERATIONS: \t", arr )

if __name__ == "__main__":
    arr = [125,2 ,52, 512, 52,1 ,52 ,125 ,52,3 ,63, 6, 7,4 ]
    print("ARRAY BEFORE SORTING: \t\t", arr)
    heapsort(arr)