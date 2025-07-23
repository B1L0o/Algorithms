def levenshtein_rec(word1, word2):

    def helper(i1, i2, n1, n2):
        if i1 == n1:
            return n2 - i2
        if i2 == n2:
            return n1 - i1
        if word1[i1] == word2[i2]:
            return helper(i1 + 1, i2 + 1, n1, n2)
        return 1 + min(helper(i1 + 1, i2, n1, n2), 
                       helper(i1, i2 + 1, n1, n2),   
                       helper(i1 + 1, i2 + 1, n1, n2))

    return helper(0,0, len(word1), len(word2))



def levenshtein(word1,word2):

    m,n = len(word1),len(word2)

    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(m):
        dp[i][0] = i 
    
    for j in range(n):
        dp[0][j] = j

    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
    
    return dp[-1][-1]


if __name__ == "__main__":
    word1 = input("Enter a word: \n" )
    word2 = input("Enter a second word:\n")
    print(f"The Levenshtein distance between {word1} and {word2} is {levenshtein(word1, word2)}.")

