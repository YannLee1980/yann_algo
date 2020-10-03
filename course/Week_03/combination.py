# 排列：
class Solution(object):
    def combine(self, n, k):
        ret = []
        self.dfs(list(range(1, n+1)), k, [], ret)
        return ret
    
    def dfs(self, nums, k, path, ret):
        if len(path) == k:
            ret.append(path)
            return 
        for i in range(len(nums)):
            print(path + [nums[i]])
            if nums[i] not in path:
                self.dfs(nums, k, path+[nums[i]], ret)

s = Solution()
print('Result:' + str(s.combine(4, 3)))