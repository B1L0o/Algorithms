# Stock management optimization - Maximum sum in an array

def kadane_opt(arr):
    m = float("-inf")
    current = 0 

    for element in arr:
        current = max(element,element + current)
        m = max(m,current)

    return m

def kadane_dp(arr):
    n=len(arr)
    dp = [0] * (n+1)
    dp[n] = float("-inf")

    for i in range(n-1,-1,-1):
        dp[i] = max(arr[i],dp[i+1] + arr[i])

    return dp[0]

    

if __name__ == "__main__":
    array = [1,2,-3,4,3,-4,-2,1]
    print(kadane_opt(array))
    print(kadane_dp(array))