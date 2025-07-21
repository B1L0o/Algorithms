# compute all pairs of distances - MSSP
from utils import dump_graph, generate_graph

def floydWarshall(n,edges):

    dist = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]
    for a,b,w in edges:
        dist[a][b] = w

    for k in range(n):
        for j in range(n):
            for i in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

if __name__ == "__main__":
    edges = generate_graph(6)
    print("final distances:", floydWarshall(6, edges))
    dump_graph(edges)


