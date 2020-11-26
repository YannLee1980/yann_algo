# 221. 最大正方形
# https://leetcode-cn.com/problems/maximal-square/
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

# 示例:

# 输入: 

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                max_side = max(max_side, dp[i][j])
                
        return max_side ** 2
                        