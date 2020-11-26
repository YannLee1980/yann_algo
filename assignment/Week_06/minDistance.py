# 72. 编辑距离
# https://leetcode-cn.com/problems/edit-distance/
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

# 你可以对一个单词进行如下三种操作：

# 插入一个字符
# 删除一个字符
# 替换一个字符
 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m * n == 0: return m + n
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # 初始化：
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # 计算DP值：
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp[i][j-1] + 1
                up = dp[i-1][j] + 1
                left_up = dp[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    left_up += 1
                dp[i][j] = min(left, up, left_up)
                
        return dp[-1][-1]
        