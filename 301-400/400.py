class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 9
        b = 1
        while n > a*b:
            n -= a*b
            a *= 10
            b += 1
        a = 10**(b-1) + (n-1)/b
        b = (n-1)%b
        return int(str(a)[b])
