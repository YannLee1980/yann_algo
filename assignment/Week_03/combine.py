# 77. 组合
# https://leetcode-cn.com/problems/combinations/
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

# 示例:

# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def DFS(nums, k, path):
            if len(path) == k:
                res.append(path)
                return None
            for i in range(len(nums)):
                DFS(nums[i+1:], k, path+[nums[i]])

        res = []
        DFS([i for i in range(1, n+1)], k, [])
        return res

s = Solution()
print(s.combine(5, 3))