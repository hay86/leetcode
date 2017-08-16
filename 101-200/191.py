class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(32):
            ret += (n>>i) & 1
        return ret
