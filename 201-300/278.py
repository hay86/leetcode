# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        l, r = 1, n
        while l<=r:
            m = int((l+r)/2)
            if isBadVersion(m):
                r = m-1
            else:
                l = m+1
        return l
