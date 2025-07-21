# Also known as DSU (Disjoint Set Union)

class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        root = self.parent[x]
        if root == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        #optimization by rank, could aslo be done by size
        if self.rank[xRoot] < self.rank[yRoot]:
            self.parent[xRoot] = yRoot
        elif self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[yRoot] = xRoot
            self.rank[xRoot] += 1

if __name__ == "__main__":
    dsu = UnionFind(10)
    dsu.union(4,5)
    dsu.union(1,9)
