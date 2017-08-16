class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        a = [[-1]*m for i in range(n)]
        a[0][0] = grid[0][0]
        for i in range(1,n+m-1):
            for j in range(m):
                if 0 <= i-j < n:
                    if 0 <= j-1:
                        a[i-j][j] = a[i-j][j-1] + grid[i-j][j]
                    if 0 <= i-j-1 and (a[i-j][j] == -1 or a[i-j-1][j] + grid[i-j][j] < a[i-j][j]):
                        a[i-j][j] = a[i-j-1][j] + grid[i-j][j]
        return a[n-1][m-1]
