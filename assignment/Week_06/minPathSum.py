# 64. 最小路径和
# https://leetcode-cn.com/problems/minimum-path-sum/

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例:

# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。

# DP 方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + gird[i][j]

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[math.inf] * (n+1) for _ in range(m+1)] # 初始值为最大值
        dp[0][1] = 0 # 第一行第二个数初始为0
        
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + grid[i][j]
                
        return dp[-1][-1]