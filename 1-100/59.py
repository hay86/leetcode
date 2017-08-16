class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0]*n for i in range(n)]
        m = int((n+1)/2)
        c4 = 1
        for i in range(m):
            p = n-2*i-1
            c1, c2, c3, c4 = c4, c4+p, c4+2*p, c4 +3*p
            for j in range(i,n-i-1):
                ret[i][j] = c1
                ret[j][n-i-1] = c2
                ret[n-i-1][n-j-1] = c3
                ret[n-j-1][i] = c4
                c1, c2, c3, c4 = c1+1, c2+1, c3+1, c4+1

        if n % 2 == 1:
            ret[m-1][m-1] = c4
        return ret
