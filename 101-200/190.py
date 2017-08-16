class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        z = 0
        for i in range(32):
            z = (z<<1) + (n&1)
            n = n>>1
        return z
