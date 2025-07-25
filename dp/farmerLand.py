# Same as Google's farmer land question  - Largest square in a matrix

# Leetcode number 221:
# Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

def maximalSquare(self, matrix):
        m,n = len(matrix),len(matrix[0])

        mat = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        max_val = 0

        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j] == 0:
                    continue
                mat[i][j] = 1 + min(mat[i-1][j-1],mat[i-1][j],mat[i][j-1])
                max_val = max(max_val,mat[i][j])
                
        if max_val != 0:
            return max_val * max_val

        for row in mat:
            for element in row:
                if element == 1:
                    return 1

        return 0
                