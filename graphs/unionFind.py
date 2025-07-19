#Also known as DSU (Disjoint Set Union)

class UnionFind:
    def __init__(self):
        self.parent = None

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, x, y):
        if self.parent[x] == self.parent[y]:
            return
        self.parent[self.parent[x]] = self.parent[y]
