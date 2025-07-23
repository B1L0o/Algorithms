import random

def knapsack(size,items):
    n=len(items)
    dp = [[0 for _ in range(size)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(size):
            if j - items[i-1][1] >= 0 and dp[i-1][j] < items[i-1][0] + dp[i-1][j - items[i-1][1]]:
                dp[i][j] = items[i-1][0] + dp[i-1][j - items[i-1][1]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp


if __name__ == "__main__":
    size=int(input("Enter backpack size: "))
    n=int(input("Enter number of items: "))
    items  = [[random.randint(10,60),random.randint(2,10)] for _ in range(n)]
    print(knapsack(size,items))