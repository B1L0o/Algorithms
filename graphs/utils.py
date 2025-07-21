import random
import matplotlib.pyplot as plt
import networkx as nx

def dump_graph(edges,oriented=True, node_size=500, font_size=12, figsize=(10, 8)):

    G = nx.DiGraph()
    for source, target, weight in edges:
        G.add_edge(source, target, weight=weight)

    plt.figure(figsize=figsize)
    pos = nx.spring_layout(G, seed=150) 

    nx.draw_networkx_nodes(G, pos, node_color='lightblue',node_size=node_size,alpha=0.5)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=font_size, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=font_size-2)

    plt.title("actual graph", fontsize=16, fontweight='bold')
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
            if random.random() < 0.15: 
                adj[i][j] = True

    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                edges.append([i,j,random.randint(1,10)])
    
    return edges


if __name__ == "__main__":

    dump_graph(generate_graph(20))