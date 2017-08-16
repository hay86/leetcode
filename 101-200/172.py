class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 0
        k = 5
        while k <= n:
            m += int(n/k)
            k = (k<<2) + k
        return m
