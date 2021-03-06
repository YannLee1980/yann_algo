# 51. N 皇后
# https://leetcode-cn.com/problems/n-queens/

# 时间复杂度：O(n!)， 空间复杂度：O(n)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(queens, pie, na):
            row = len(queens)
            if row == n:
                results.append(queens)
                return None
            for col in range(n):
                if col not in queens and row+col not in pie and row-col not in na:
                    dfs(queens+[col], pie+[row+col], na+[row-col])
        
        results = []
        dfs([], [], [])
        return [[f"{'.'*i}Q{'.'*(n-i-1)}" for i in res] for res in results]