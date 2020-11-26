# 52. N皇后 II
# https://leetcode-cn.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row, cols, pie, na):
            if row == n:
                nonlocal count
                count += 1
                return None
            bits = (~(cols | pie | na)) & ((1 << n) -1)
            
            while bits:
                p = bits & (-bits)
                bits &= bits - 1
                dfs(row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
        
        count = 0
        dfs(0, 0, 0, 0)
        return count