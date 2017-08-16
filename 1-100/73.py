class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        firstRow, firstCol = False, False
        for i in range(c):
            if matrix[0][i] is 0:
                firstRow = True
                break
        for i in range(r):
            if matrix[i][0] is 0:
                firstCol = True
                break        
        for i in range(1, r):
            for j in range(1, c):
                if matrix[i][j] is 0:
                    if matrix[i][0] is not 0:
                        matrix[i][0] = 0
                    if matrix[0][j] is not 0:
                        matrix[0][j] = 0
        for k in range(1,r):
            if matrix[k][0] is 0:
                for l in range(1,c):
                    if matrix[k][l] is not 0:
                        matrix[k][l] = 0
        for k in range(1,c):
            if matrix[0][k] is 0:
                for l in range(1,r):
                    if matrix[l][k] is not 0:
                        matrix[l][k] = 0
        if firstRow:
            for l in range(c):
                if matrix[0][l] is not 0:
                    matrix[0][l] = 0
        if firstCol:
            for l in range(r):
                if matrix[l][0] is not 0:
                    matrix[l][0] = 0
            
                
