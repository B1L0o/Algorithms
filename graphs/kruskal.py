from unionFind import UnionFind

import heapq

def kruskal(n, edges):
    DSU = UnionFind(n)
    forest = set()
    pq = []
    for x,y,w in edges:
        #DSU needs integers to work 
        a=ord(x) - ord('A')
        b=ord(y) - ord('A')
        heapq.heappush(pq,(w,[a,b])) 
    while pq:
        w,[a,b] = heapq.heappop(pq)
        if DSU.find(a) != DSU.find(b):
            #Converst to letters for output
            x = chr(a + ord('A'))
            y = chr(b + ord('A'))
            edge = str(x) + "->" + str(y)
            forest.add(edge)
            DSU.union(a,b)
    return forest


if __name__ == "__main__":
    edges = [
        ('A', 'B', 7),
        ('A', 'D', 5),
        ('B', 'D', 9),
        ('B', 'C', 8),
        ('B', 'E', 7),
        ('D', 'E', 15),
        ('D', 'F', 6),
        ('C', 'E', 5),
        ('E', 'F', 8),
        ('F', 'G', 11),
        ('E', 'G', 9)
    ]

    res = kruskal(7,edges)
    print(res)