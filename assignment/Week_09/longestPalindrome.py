# 5. 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# https://leetcode-cn.com/problems/longest-palindromic-substring/

# DP:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j-i<2 or dp[i+1][j-1])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j+1]
        
        return res
        
# 枚举中心，两边扩散:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def _extendPalin(i, j):
            nonlocal lo, max_len
        
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            if j - i - 1 > max_len:
                lo = i + 1
                max_len = j - i - 1
            
        n = len(s)
        if n < 2: return s
        lo, max_len = 0, 0
        
        for i in range(n):
            _extendPalin(i, i)
            _extendPalin(i, i+1)
            
        return s[lo: lo+max_len]