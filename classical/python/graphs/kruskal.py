from unionFind import UnionFind
from utils import dump_graph, generate_graph

import heapq

def kruskal(n, edges):
    DSU = UnionFind(n)
    forest = []
    pq = []

    for a,b,w in edges:
        heapq.heappush(pq,(w,[a,b])) 

    while pq:
        w,[a,b] = heapq.heappop(pq)
        if DSU.find(a) != DSU.find(b):
            DSU.union(a,b)
            forest.append([a,b,w])

    return forest

if __name__ == "__main__":
    n=int(input("\nEnter number of nodes for the graph: \n\n> "))
    edges = generate_graph(n)
    forest = kruskal(n,edges)
    print("\n[ Graph preview ... ]\n")
    dump_graph(n,edges,oriented=False)
    print("[ MST preview ...]\n")
    dump_graph(n,forest,oriented=False,name="Minimal Spanning Tree")