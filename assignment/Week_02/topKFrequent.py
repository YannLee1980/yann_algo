# 347. 前 K 
# https://leetcode-cn.com/problems/top-k-frequent-elements/
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

 

# 示例 1:

# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:

# 输入: nums = [1], k = 1
# 输出: [1]
 

from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        heapq = PriorityQueue()
        num_set = set(nums)
        cnt_dict = {}
        
        for n in num_set: cnt_dict[n] = 0
        for n in nums: cnt_dict[n] -= 1
        
        for n in cnt_dict.keys():
            heapq.put((cnt_dict[n], n))
        
        for _ in range(k):
            res.append(heapq.get()[1])
        
        return res