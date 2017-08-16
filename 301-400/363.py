import bisect

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        if n == 0:
            return 0
        m = len(matrix[0])
        if m == 0:
            return 0
        
        if n > m:
            tmp = [[0]*(n+1) for i in range(m+1)]
            for i in range(n):
                for j in range(m):
                    tmp[j+1][i+1] = matrix[i][j]
            n, m = m, n
        else:
            tmp = [[0]*(m+1) for i in range(n+1)]
            for i in range(n):
                for j in range(m):
                    tmp[i+1][j+1] = matrix[i][j]
        matrix = tmp
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        
        ret = -2147483648
        for i in range(1,n+1):
            for j in range(i):
                buf = [0]
                for kk in range(1,m+1):
                    y = matrix[i][kk] - matrix[j][kk]
                    p = bisect.bisect_left(buf, y-k)
                    if p < len(buf):
                        a, b = k-ret, k-y+buf[p]
                        if b == 0:
                            return k
                        elif a > b:
                            ret = y-buf[p]
                    bisect.insort(buf, y)
                    
        return ret
