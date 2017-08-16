import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            x = math.log(n, 3)
            return pow(3, round(x)) == n
        return False
