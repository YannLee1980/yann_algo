class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        if len(nums) < 4: return []
        nums.sort()
        res = []
        
        for l in range(len(nums)-3):
            if nums[l] > target: break
            if l > 0 and nums[l] == nums[l-1]: continue
            for k in range(l+1, len(nums)-2):
                if nums[k] > target - nums[l]: break
                if k > l + 1 and nums[k] == nums[k-1]: continue
                i, j = k + 1, len(nums) - 1
                while i < j:
                    s = nums[i] + nums[j] + nums[k] + nums[l]
                    if s < target:
                        i += 1
                        while i < j and nums[i-1] == nums[i]: i += 1
                    elif s > target:
                        j -= 1
                        while i < j and nums[j+1] == nums[j]: j -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        i += 1
                        j -= 1
                        while i < j and nums[i-1] == nums[i]: i += 1
                        while i < j and nums[j+1] == nums[j]: j -= 1
                    
        return res

s = Solution()
print(s.fourSum([1,-2,-5,-4,-3,3,3,5], -11))