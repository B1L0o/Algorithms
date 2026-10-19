# Maximize profit but not allowed to rob two adjacent houses

# This is leetcode problem 740 (same idea:):
# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

def houseRobber(houses):
    n=max(houses)+2
    money=[0] * n 
    for house in houses:
        money += house 

    dp=[0] * n+1
    for i in range(n-2,-1,-1):
        dp[i] = max(dp[i+1], dp[i+2] + money[i])
    
    return max(dp[0],dp[1])
