class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid)
        if w == 0:
            return 0
        h = len(grid[0])
        ret = 0
        for i in range(w):
            for j in range(h):
                if grid[i][j] == 1:
                    if i==0 or grid[i-1][j] == 0:
                        ret += 1
                    if i==w-1 or grid[i+1][j] == 0:
                        ret += 1
                    if j==0 or grid[i][j-1] == 0:
                        ret += 1
                    if j==h-1 or grid[i][j+1] == 0:
                        ret += 1
        return ret