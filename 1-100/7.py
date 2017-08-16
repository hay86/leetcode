class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = -1 if x < 0 else 1
        x = abs(x)
        z = 0
        while x > 0:
            z = z*10 + x % 10
            x = int(x/10)
        return 0 if z > 2147483647 else z*y
