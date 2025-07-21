# worse than djikstra but works with negative cycles - SSSP
from utils import dump_graph, generate_graph

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
    size = int(input("Enter number of nodes:\n"))
    edges = generate_graph(size)
    print("[======= Final distances ======]\n", bellmanford(size, edges,0))
    dump_graph(size,edges)
