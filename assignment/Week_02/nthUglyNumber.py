# 剑指 Offer 49. 丑数
# https://leetcode-cn.com/problems/chou-shu-lcof/
# 我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

# 示例:

# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 说明:  

# 1 是丑数。
# n 不超过1690。

import heapq

class UglyNumber:
    def __init__(self):
        seen = {1, }
        self.nums = []
        heap = []
        heapq.heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heapq.heappop(heap)
            self.nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

class Solution:
    uglynumber = UglyNumber()
    def nthUglyNumber(self, n: int) -> int:
        return self.uglynumber.nums[n-1]

s = Solution()
print(s.nthUglyNumber(10))
print(s.nthUglyNumber(15))
print(s.nthUglyNumber(20))
