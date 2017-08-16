import math

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        ret = math.log(num,2)
        iret = int(ret)
        return ret == iret and iret % 2 == 0
        
