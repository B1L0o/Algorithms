# best but only works without negatives cycles - SSSP
from utils import dump_graph, generate_graph

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
            if w1 + w2 < dist[v2]:
                dist[v2] = w1 + w2
                heapq.heappush(pq, (w1 + w2, v2))

    return dist

if __name__ == "__main__":
    size = int(input("\nEnter number of nodes:\n\n> "))
    edges = generate_graph(size)

    while True:
        key = input("\nSelect the starting node: \t\t(Type 'quit' to exit)\n\n> ")
        if key == "quit":
            exit()

        src = int(key)
        D=djikstra(size, edges,src)
        print("\n\t[======= Final distances ======]\n")
        for i in range(len(D)):
            if i == src:
                continue
            print(f"The shortest distance between the nodes\t\t{src}\tand\t{i}\tis\t[{D[i]}]")
        print("\n[graph in preview...]\n\n")
        dump_graph(size,edges)
