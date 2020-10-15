class Solution:
    def subsets(self, nums: list) -> list:
        def dfs(nums, index, path):
            if index == len(nums):
                res.append(path)
                return None
            dfs(nums, index+1, path.copy())
            path.append(nums[index])
            dfs(nums, index+1, path.copy())
        
        res = []
        dfs(nums, 0, [])
        return res

s = Solution()
print(s.subsets([1,2,3]))
