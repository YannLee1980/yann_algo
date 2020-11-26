class SelectionSort:
    def selectionSort(self, nums):
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [3,5,446,7,0,-498,9,4,-5,6,7]
s = SelectionSort()
s.selectionSort(nums)
print(nums)