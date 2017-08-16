class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = x
        n = 0
        while y > 0:
            y = int(y/10)
            n += 1
        l, r = 1, 10**(n-1)
        size = int(n/2)
        for i in range(size):
            if int(x/l)%10 != int(x/r)%10:
                return False
            l *= 10
            r /= 10
        return True
