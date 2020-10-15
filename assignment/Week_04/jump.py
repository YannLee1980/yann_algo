# 45. 跳跃游戏 II
# https://leetcode-cn.com/problems/jump-game-ii/
# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。

# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n-1):
            if maxPos >= i:
                maxPos = max(maxPos, nums[i]+i)
                if i == end: # 关键：贪心的体验，选遇到的最优step才加1.
                    end = maxPos
                    step += 1
        return step