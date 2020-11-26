# 归并排序：

class MergeSort:
    def mergesort(self, nums, left, right):
        if left >= right:
            return None
        mid = (left + right) >> 1  # (left+right) // 2
        self.mergesort(nums, left, mid)
        self.mergesort(nums, mid + 1, right)
        self._merge(nums, left, mid, right)

    def _merge(self, nums, left, mid, right):
        tmp = []
        i = left

        for j in range(mid+1, right+1):
            while i <= mid and nums[i] <= nums[j]:
                tmp.append(nums[i])
                i += 1
            tmp.append(nums[j])
        while i <= mid:
            tmp.append(nums[i])
            i += 1
        nums[left:right+1] = tmp


a = [3,5,446,7,0,-498,9,4,-5,633,7]
q = MergeSort()
q.mergesort(a, 0, len(a)-1)
print(a)