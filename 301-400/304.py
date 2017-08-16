class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m > 0 else 0
        self.s = [[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.s[i+1][j+1] = self.s[i+1][j] + self.s[i][j+1] - self.s[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.s[row2+1][col2+1] - self.s[row2+1][col1] - self.s[row1][col2+1] + self.s[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
