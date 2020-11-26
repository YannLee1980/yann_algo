class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p: return True
        m, n = len(s), len(p)
        memo = [[0] * (n + 1) for _ in range(m + 1)]
        
        def dp(i, j):
            if memo[i][j] != 0: return memo[i][j]
            if j == len(p): return i == len(s)
            
            first = len(s) > i and p[j] in [s[i], '?']
            
            if len(p) > j and p[j] == '*':
                ans = False
                for k in range(i, len(s)+1):
                    ans = ans or dp(k, j+1)
            else:
                ans = first and dp(i+1, j+1)
            memo[i][j] = ans
            
            return ans
        
        return dp(0, 0)

s = Solution()
print(s.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b"))