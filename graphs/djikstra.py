import heapq

def djikstra(n, edges, src):
    dist = [float("inf")] * n
    visited = [False] * n
    adj = {i: [] for i in range(n)}
    for a,b,w in edges:
        adj[a].append([w,b])
    
    dist[src] = 0
    pq = [(0, src)]

    while len(pq) > 0:
        w1, v1 = heapq.heappop(pq)

        if visited[v1]:
            continue

        visited[v1] = True
        for w2, v2 in adj[v1]:
            heapq.heappush(pq, (w1 + w2, v2))
            if w1 + w2 < dist[v2]:
                dist[v2] = w1 + w2
    return dist

if __name__ == "__main__":
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2),
        (3, 5, 6),
        (4, 5, 3)
    ]

    print("final distances:", djikstra(6, edges, 0))
