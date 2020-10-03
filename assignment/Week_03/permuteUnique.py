# 47. 全排列 II
# https://leetcode-cn.com/problems/permutations-ii/
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。

# 示例:

# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution:
    def permuteUnique(self, nums: list) -> list:
        def DFS(nums, n, path):
            if len(path) == n and path not in res:
                res.append(path)
                return None
            for i in range(len(nums)):
                new_nums = nums.copy()
                new_nums.pop(i)
                DFS(new_nums, n, path+[nums[i]])
        
        res = []
        DFS(nums, len(nums), [])
        return res

s = Solution()
print(s.permuteUnique([1,1,2]))