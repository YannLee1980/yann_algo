# 1122. 数组的相对排序
# https://leetcode-cn.com/problems/relative-sort-array/

# 计数排序
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = [0] * 1001
        res = []
        for a1 in arr1:
            counter[a1] += 1
        for a2 in arr2:
            while counter[a2] > 0:
                res.append(a2)
                counter[a2] -= 1
        for i in range(len(counter)):
            while counter[i] > 0:
                res.append(i)
                counter[i] -= 1
        return res