# Also known as DSU (Disjoint Set Union)

class UnionFind:

    def __init__(self,n):
        self.parents = [-1] * n


    def find(self,x):
        if self.parents[x] < 0:
            return x

        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


    def union(self,x,y):
        p1= self.find(x)
        p2= self.find(y)

        if p1 == p2:
            return

        size1 = self.parents[p1] * -1
        size2 = self.parents[p2] * -1

        if size1 < size2:
            self.parents[p1] = p2
            self.parents[p2] = ( size1 + size2 ) * -1
        else:
            self.parents[p2] = p1
            self.parents[p1] = ( size1 + size2 ) * -1


if __name__ == "__main__":
    dsu = UnionFind(10)
    dsu.union(4,5)
    dsu.union(1,9)