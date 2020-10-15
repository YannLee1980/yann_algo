# 74. 搜索二维矩阵
# https://leetcode-cn.com/problems/search-a-2d-matrix/
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nr = len(matrix)
        if nr == 0:
            return False
        nc = len(matrix[0])
        left, right = 0, nc * nr -1
        
        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid//nc][mid%nc]
            if mid_element == target:
                return True
            elif target < mid_element:
                right = mid - 1
            else:
                left = mid + 1
            
        return False