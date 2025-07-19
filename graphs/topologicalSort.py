def topologicalSort(n, edges):
    seen = [False] * n
    visited = [False] * n

    answer = []

    adj = {i:[] for i in range(n)}

    for a, b in edges:
        adj[a].append(b)

    for vertex in range(n):
        for dep in adj[vertex]:
            visited[vertex] = True
