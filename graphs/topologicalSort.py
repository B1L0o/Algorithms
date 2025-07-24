def topologicalSort(n, edges):
    adj = {i: [] for i in range(n)}
    for a, b in edges:
        adj[a].append(b) 

    visited = [0] * n  
    answer = []
    has_cycle = [False]

    def dfs(node):
        if visited[node] == 1:
            has_cycle[0] = True
            return
        if visited[node] == 2:
            return

        visited[node] = 1  
        for neighbor in adj[node]:
            dfs(neighbor)
        visited[node] = 2  
        answer.append(node)

    for vertex in range(n):
        if visited[vertex] == 0:
            dfs(vertex)

    if has_cycle[0]:
        return [] 
    # reversed order 
    return answer[::-1] 
