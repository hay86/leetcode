class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 1:
            return 1
        i = 1
        while i <= num:
            i <<= 1
        return (i-1) ^ num