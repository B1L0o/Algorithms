import random
import matplotlib.pyplot as plt
import networkx as nx

def dump_graph(n,edges, oriented=True, node_size=500, font_size=12, figsize=(20, 10),name="Graph Preview"):
    G = nx.DiGraph() if oriented else nx.Graph()

    for source, target, weight in edges:
        G.add_edge(source, target, weight=weight)

    plt.figure(figsize=figsize)
    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color=range(n), node_size=node_size, alpha=0.5)
    nx.draw_networkx_edges(G, pos, arrows=oriented)
    nx.draw_networkx_labels(G, pos, font_size=font_size, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=font_size - 2)

    plt.title(name, fontsize=16, fontweight='bold')
    plt.axis("off")
    plt.show()

def generate_graph(n):
    adj = [[False for _ in range(n)] for _ in range(n)]
    edges=[]

    for i in range(n):
        r = random.randint(0,n-1)
        while r == i:
            r = random.randint(0,n-1)
        adj[i][r] = True
        for j in range(n):
            if i == j:
                continue
            if random.random() < 1/n: 
                adj[i][j] = True

    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                edges.append([i,j,random.randint(1,10)])
    
    return edges


if __name__ == "__main__":
    size=int(input("enter number of nodes: "))
    dump_graph(size,generate_graph(size))