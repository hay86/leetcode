class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        a = [[0]*m for i in range(n)]
        a[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1,n+m-1):
            for j in range(m):
                if 0 <= i-j < n and obstacleGrid[i-j][j] == 0:
                    if 0 <= j-1:
                        a[i-j][j] += a[i-j][j-1]
                    if 0 <= i-j-1:
                        a[i-j][j] += a[i-j-1][j]
        return a[n-1][m-1]
