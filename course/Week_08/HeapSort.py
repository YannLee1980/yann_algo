# 堆排序：
import heapq
class HeapSort:
    def heapSort(self, nums):
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
        for i in range(len(nums)):
            nums[i] = heapq.heappop(heap)

a = [3,5,6,-897,38,-9,4,5,633,7]
q = HeapSort()
q.heapSort(a)
print(a)