# 200. 岛屿数量
# https://leetcode-cn.com/problems/number-of-islands/
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

# 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

# 此外，你可以假设该网格的四条边均被水包围。

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            grid[row][col] = '0'
            for x, y in [(row, col-1), (row, col+1), (row-1, col), (row+1, col)]:
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                    dfs(x, y)
                    
        nr = len(grid)
        if nr == 0: return 0
        nc = len(grid[0])
        min_islands = 0

        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == '1':
                    min_islands += 1
                    dfs(row, col)
                    
        return min_islands