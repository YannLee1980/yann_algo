# 55. 跳跃游戏
# https://leetcode-cn.com/problems/jump-game/
# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 判断你是否能够到达最后一个位置。

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        reachable = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= reachable:
                reachable = i
        if reachable == 0:
            return True
        else:
            return False