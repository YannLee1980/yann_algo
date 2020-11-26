# 32. 最长有效括号
# https://leetcode-cn.com/problems/longest-valid-parentheses/
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1: return 0
        
        dp = [0] * n
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i>1 else 0) + 2
                elif i-dp[i-1]>=1 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]>=2 else 0) + 2
                
        return max(dp)