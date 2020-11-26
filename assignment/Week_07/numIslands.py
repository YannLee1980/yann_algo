# 200. 岛屿数量
# https://leetcode-cn.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def _union(p, i, j):
            p1 = _parent(p, i)
            p2 = _parent(p, j)
            if p1 == p2: return None
            p[p1] = p2
            nonlocal count
            count -= 1

        def _parent(p, i):
            root = i
            while p[root] != root:
                root = p[root]
            while p[i] != i:
                x = i
                i = p[i]
                p[x] = root
            return root
        
        if not grid: return 0
        m = len(grid)
        n = len(grid[0])
        p = [-1] * (m * n)
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    p[i * n + j] = i * n + j
                    count += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if i+1 < m and grid[i+1][j] == '1':
                        _union(p, i*n+j, (i+1)*n+j)
                    if j+1 < n and grid[i][j+1] == '1':
                        _union(p, i*n+j, i*n+j+1)

        return count