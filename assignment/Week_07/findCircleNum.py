# 547. 朋友圈
# https://leetcode-cn.com/problems/friend-circles/

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def dfs(m, visited, i):
            for j in range(n):
                if m[i][j] == 1 and visited[j] is False:
                    visited[j] = True
                    dfs(m, visited, j)
        
        if not M: return 0
        n = len(M)
        res = 0
        visited = [False] * n
        
        for i in range(n):
            if visited[i] is False:
                dfs(M, visited, i)
                res += 1
            
        return res