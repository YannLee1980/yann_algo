# 115. 不同的子序列
# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
# https://leetcode-cn.com/problems/distinct-subsequences/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s or not t: return 0
        
        m, n = len(t), len(s)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(n + 1):
            dp[0][i] = 1
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
                    
        return dp[-1][-1]