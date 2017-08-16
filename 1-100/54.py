class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        if m == 0 or n == 0:
            return ret
        x, y, dx, dy = 0, 0, 0, 1
        up, down, left, right = 0, m-1, 0, n-1
        while up <= down and left <= right:
            ret.append(matrix[x][y])
            if dy == 1 and y == right:
                dx, dy = 1, 0
                up += 1
            elif dx == 1 and x == down:
                dx, dy = 0, -1
                right -= 1
            elif dy == -1 and y == left:
                dx, dy = -1, 0
                down -= 1
            elif dx == -1 and x == up:
                dx, dy = 0, 1
                left += 1
            x, y = x+dx, y+dy
        return ret
