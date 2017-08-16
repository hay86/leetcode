class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        w = len(grid)
        h = len(grid[0]) if w > 0 else 0
        ret = 0
        for i in range(w):
            for j in range(h):
                if grid[i][j] == '1':
                    ret += 1
                    self.dfs(grid, i, j, w, h)
        return ret
        
    def dfs(self, grid, i, j, w, h):
        grid[i][j] = '0'
        if i-1 >= 0 and grid[i-1][j] == '1':
            self.dfs(grid, i-1, j, w, h)
        if i+1 < w and grid[i+1][j] == '1':
            self.dfs(grid, i+1, j, w, h)
        if j-1 >= 0 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1, w, h)
        if j+1 < h and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1, w, h)
