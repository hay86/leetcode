class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        l,r = 0, num
        while l <= r:
            m = (l+r)/2
            mm = m*m
            if mm == num:
                return True
            elif mm > num:
                r = m-1
            else:
                l = m+1
        return False
