# 快速排序：

class QuickSort:
    def quickSort(self, begin, end, nums):
        if begin >= end: return None
        pivot = self._partition(begin, end, nums)
        self.quickSort(begin, pivot - 1, nums)
        self.quickSort(pivot + 1, end, nums)

    def _partition(self, begin, end, nums):
        pivot = end
        counter = begin
        for i in range(begin, end):
            if nums[i] < nums[pivot]:
                nums[i], nums[counter] = nums[counter], nums[i]
                counter += 1
        nums[counter], nums[pivot] = nums[pivot], nums[counter]
        return counter


a = [3,5,6,7,8,9,4,5,6,7]
q = QuickSort()
q.quickSort(0, len(a)-1, a)
print(a)