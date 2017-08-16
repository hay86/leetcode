class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = int(n**0.5)
        if m*m == n:
            return 1
        while n%4 == 0:
            n /= 4
        if n%8 == 7:
            return 4
        m = int(n**0.5)
        for i in range(1,m+1):
            k = int((n-i*i)**0.5)
            if k*k + i*i == n:
                return 2
        return 3
