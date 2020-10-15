# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 或 3个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        if n == 3: return 4
        f1, f2, f3, dp = 1, 2, 4, 0
        for _ in range(4, n+1):
            dp = f1 + f2 + f3
            f1 = f2
            f2 = f3
            f3 = dp
        return dp

s = Solution()
print(s.climbStairs(10))