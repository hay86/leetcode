"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if len(grid) == 0:
            return None
        return self.dfs(grid, 0, 0, len(grid))
        
    def dfs(self, grid, x, y, a):
        s = sum([sum(row[y:y+a]) for row in grid[x:x+a]])
        if s == 0:
            return Node(False, True, None, None, None, None)
        elif s == a*a:
            return Node(True, True, None, None, None, None)
        else:
            return Node(True, False, self.dfs(grid, x, y, a/2), self.dfs(grid, x, y+a/2, a/2), self.dfs(grid, x+a/2, y, a/2), self.dfs(grid, x+a/2, y+a/2, a/2))
