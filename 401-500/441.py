class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = int((2*n)**0.5)
        if k*(k+1) > 2*n:
            return k-1
        else:
            return k