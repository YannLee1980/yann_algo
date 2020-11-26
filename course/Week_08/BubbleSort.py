class BubbleSort:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(n-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [3,5,446,7,0,-498,9,4,-5,6,7]
s = BubbleSort()
s.bubbleSort(nums)
print(nums)