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
    size = int(input("\nEnter number of nodes:\n\n> "))
    edges = generate_graph(size)

    while True:
        key = input("\nSelect the starting node: \t\t(Type 'quit' to exit)\n\n> ")
        if key == "quit":
            exit()

        src = int(key)
        D=bellmanford(size, edges,src)
        print("\n\t[======= Final distances ======]\n")
        for i in range(len(D)):
            if i == src:
                continue
            print(f"The shortest distance between the nodes\t\t{src}\tand\t{i}\tis\t[{D[i]}]")
        print("\n[graph in preview...]\n\n")
        dump_graph(size,edges)