from unionFind import UnionFind
from utils import dump_graph, generate_graph

import heapq

def kruskal(n, edges):
    DSU = UnionFind(n)
    forest = set()
    res=[]
    pq = []
    for a,b,w in edges:
        heapq.heappush(pq,(w,[a,b])) 
    while pq:
        w,[a,b] = heapq.heappop(pq)
        if DSU.find(a) != DSU.find(b):
            DSU.union(a,b)
            edge = str(a) + "->" + str(b)
            forest.add(edge)
            res.append([a,b,w])
    return forest,res


if __name__ == "__main__":
    n=int(input("number of edges in the graph: "))
    edges = generate_graph(n)
    forest,res = kruskal(n,edges)
    print(forest)
    dump_graph(n,edges,oriented=False)
    dump_graph(n,res,oriented=False)