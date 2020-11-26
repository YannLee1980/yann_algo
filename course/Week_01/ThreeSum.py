class Solution:
    def (self, nums: list) -> list:
        result = []
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        tmp = [nums[i], nums[j], nums[k]]
                        if len(result) == 0:
                            result.append(tmp)
                        else:
                            for l in result:
                                if sorted(l) == sorted(tmp):
                                    break
                                result.append(tmp)
        return result

s = Solution()
print(s.([-1, 0, 1, 2, -1, -4]))