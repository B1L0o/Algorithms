import heapq

def heapsort(arr):
    n=len(arr)
    pq = []

    for element in arr:
        heapq.heappush(pq,element)

    for i in range(n):
        arr[i] = heapq.heappop(pq)