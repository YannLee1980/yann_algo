class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 0 # 指针记录最终结果
        
        if len(nums) == 0:
            return 0
        
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] , nums[j] = nums[j] , nums[i]
                
        return i + 1

s = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(nums))