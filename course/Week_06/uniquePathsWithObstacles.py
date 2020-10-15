class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # initialize:
        cur = [0] * n
        
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    cur[j] = 0
                elif j == 0 and cur[j] : 
                    cur[j] = 1
                else:
                    cur[j] += cur[j-1]
                    
        return cur[-1]

s = Solution()
print(s.uniquePathsWithObstacles([[1],[0]]))