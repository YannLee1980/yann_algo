class Solution:
    def checkRecord(self, n: int) -> int:
        def dfs(path):
            if len(path) == n:
                print(path)
                if path.count('A') <= 1 and path.count('L') <= 2:
                    res[0] += 1
                return None
            dfs(path+'A')
            dfs(path+'L')
            dfs(path+'P')
        
        res = [0]
        dfs('')
        return res

s = Solution()
print(s.checkRecord(2))