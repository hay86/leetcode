class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=[1,1]
        for i in range(2, n+1):
            a.append(a[i-1]+a[i-2])
        return a[n]
