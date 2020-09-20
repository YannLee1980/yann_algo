class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]] , i]
            else:
                buff_dict[target - nums[i]] = i
        return False

s = Solution()
s.twoSum([21,7,11,15], 18)