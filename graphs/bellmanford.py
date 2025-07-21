def bellmanford(n,edges,src):
    dist = [float("inf")] * n 
    dist[src] = 0
    for _ in range(n):
        for ingoing,outgoing,weight in edges:
            if dist[ingoing] + weight < dist[outgoing]:
                dist[outgoing] = dist[ingoing] + weight
    
    for _ in range(n):
        for ingoing,outgoing,weight in edges:
            if dist[ingoing] + weight < dist[outgoing]:
                dist[outgoing] = float("-inf")
    
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

    print("final distances:", bellmanford(6, edges, 0))
