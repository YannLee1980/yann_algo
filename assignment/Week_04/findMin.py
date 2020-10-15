# 153. 寻找旋转排序数组中的最小值
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 请找出其中最小的元素。

# 你可以假设数组中不存在重复元素。

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums)-1
        
        if nums[left] < nums[right]:
            return nums[left]
        
        while left < right:
            mid = (left + right) // 2
            # 下面的两个if缺一不可，否则会出现有return None的情况。
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[0] < nums[mid]:
                left = mid + 1
            else:
                right = mid -1