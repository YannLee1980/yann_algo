class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        left, right = 0 , m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            if target == matrix[mid//n][mid%n]:
                return True
            elif target > matrix[mid//n][mid%n]:
                left = mid + 1
            else:
                right = mid -1
                
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))