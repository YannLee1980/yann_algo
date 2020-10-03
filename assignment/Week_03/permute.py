# 46. 全排列
# https://leetcode-cn.com/problems/permutations/
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def DFS(nums, path):
            if len(path) == len(nums):
                res.append(path)
                return None
            for i in range(len(nums)):
                if nums[i] not in path:
                    DFS(nums, path+[nums[i]])

        res = []
        DFS(nums, [])
        return res