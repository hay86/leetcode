class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = [[0]*m for i in range(n)]
        a[0][0] = 1
        for i in range(1,n+m-1):
            for j in range(m):
                if 0 <= i-j < n:
                    if 0 <= j-1:
                        a[i-j][j] += a[i-j][j-1]
                    if 0 <= i-j-1:
                        a[i-j][j] += a[i-j-1][j]
        return a[n-1][m-1]
