class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        n = len(matrix)
        m = len(matrix[0])
        i, j = 0, m-1
        while i < n and j >= 0:
            x = matrix[i][j]
            if x == target:
                return True
            elif x > target:
                j -= 1
            else:
                i += 1
        return False
