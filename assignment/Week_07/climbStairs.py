# 70. 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/

# 记忆化搜索 + LRU_cache:
from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache
        def dfs(n):
            return dfs(n - 1) + dfs(n - 2) if n > 2 else n
        
        return dfs(n)