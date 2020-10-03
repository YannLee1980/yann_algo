
class Solution:
    def subsets(self, nums: list) -> list:
        res = []
        self.dfs(nums, [], 0, res)
        return res
    
    def dfs(self, nums, path, index, res):
        if index == len(nums):
            res.append(path)
            return
        
        self.dfs(nums, path, index+1, res)
        
        path.append(nums[index])
        print(f'index:{index}')
        self.dfs(nums, path, index+1, res)

        
s = Solution()
print(s.subsets([1,2,3]))