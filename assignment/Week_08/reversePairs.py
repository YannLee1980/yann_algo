# 493. 翻转对
# https://leetcode-cn.com/problems/reverse-pairs/

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if not nums: return 0
        return self._mergeSort(nums, 0, len(nums)-1)
        
    def _mergeSort(self, nums, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        count = self._mergeSort(nums, left, mid) + self._mergeSort(nums, mid+1, right)
        cache = []
        i, k = left, left
        for j in range(mid+1, right+1):
            while k <= mid and nums[k]/2.0 <= nums[j]:
                k += 1
            while i <= mid and nums[i] < nums[j]:
                cache.append(nums[i])
                i += 1
            cache.append(nums[j])
            count += mid - k +1
        while i <= mid:
            cache.append(nums[i])
            i += 1
        nums[left: right+1] = cache
        return count
        