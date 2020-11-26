class InsertionSort:
    def insertionSort(self, nums):
        n = len(nums)
        pre_index = 0
        current = 0
        for i in range(1, n):
            pre_index = i-1
            current = nums[i]
            while pre_index >= 0 and nums[pre_index] > current:
                nums[pre_index+1] = nums[pre_index]
                pre_index -= 1
            nums[pre_index+1] = current


a = [3,5,446,7,0,-498,9,4,-5,6,7]
q = InsertionSort()
q.insertionSort(a)
print(a)