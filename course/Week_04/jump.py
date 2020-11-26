class Solution:
    def jump(self, nums: list) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n):
            if maxPos >= i and i < n - 1:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
            else:
                return -1
        return step

s = Solution()
print(s.jump([2,2,1,1,4]))