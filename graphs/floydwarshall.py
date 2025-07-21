def floydWarshall(n,edges):

    dp = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]
    for a,b,w in edges:
        dp[a][b] = w

    for k in range(n):
        for j in range(n):
            for i in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

if __name__ == "__main__":
    edges = [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 1),
        (1, 3, 5),
        (2, 3, 8),
        (2, 4, 10),
        (3, 4, 2),
        (3, 5, 6),
        (4, 5, 3)
    ]

    print("final distances:", floydWarshall(6, edges))

