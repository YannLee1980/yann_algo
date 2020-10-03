class Solution:
    def permuteUnique(self, nums: list) -> list:
        n = len(nums)
        res = []
        self.dfs(nums, n, [], res)
        return res
    
    def dfs(self, nums, n, path, res):
        if len(path) == n:
            res.append(path)
            return
        
        for i in range(len(nums)):
            if nums[i] not in path: 
                self.dfs(nums, n, path+[nums[i]], res)

s = Solution()
print(s.permuteUnique([1,2,1]))