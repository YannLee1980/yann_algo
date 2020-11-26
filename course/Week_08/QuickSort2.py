class QuickSort:
    def quickSort(self, nums, begin, end):
        """
        docstring
        """
        if begin >= end:
            return None
        pivot = self._partition(nums, begin, end)
        self.quickSort(nums, begin, pivot - 1)
        self.quickSort(nums, pivot + 1, end)

    def _partition(self, nums, begin, end):
        pivot = end
        counter = begin
        for i in range(begin, end):
            if nums[i] < nums[pivot]:
                nums[i], nums[counter] = nums[counter], nums[i]
                counter += 1
        nums[pivot], nums[counter] = nums[counter], nums[pivot]
        return counter

a = [3,5,63,71,834,9,-34,5,-6,-7]
q = QuickSort()
q.quickSort(a, 0, len(a)-1)
print(a)