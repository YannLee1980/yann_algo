# 33. 搜索旋转排序数组
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

# 你可以假设数组中不存在重复的元素。

# 你的算法时间复杂度必须是 O(log n) 级别。

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[0] <= nums[mid] and (target > nums[mid] or target < nums[0]):
                left = mid + 1
            elif target < nums[0] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left if left == right and nums[left] == target else -1
            