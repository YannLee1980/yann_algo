# 647. 回文子串
# https://leetcode-cn.com/problems/palindromic-substrings/
# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

# 具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

# 参考：https://leetcode-cn.com/problems/palindromic-substrings/solution/liang-dao-hui-wen-zi-chuan-de-jie-fa-xiang-jie-zho/

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        
        dp = [[False] * n for _ in range(n)] # dp[i][j] 表示s[i:j+1]是不是回文
        res = 0
        
        for j in range(n):
            for i in range(j+1):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]): # 两个字符长时看看前后相不相等，超过两个长时，去掉最后一个，看剩下的等不等。
                    dp[i][j] = True
                    res += 1
                    
        return res