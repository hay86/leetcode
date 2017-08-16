class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        b = [True]*n
        b[0] = False
        b[1] = False
        m = int(n**0.5)
        for i in range(2, m+1):
            if b[i]:
                for j in range(i*i, n, i):
                    b[j] = False
        c = 0 
        for i in range(n):
            if b[i]:
                c += 1
        return c
