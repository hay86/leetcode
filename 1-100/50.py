class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans = 1
        m = abs(n)
        while m > 0:
            if m%2 == 1:
                ans *= x
            m = m>>1
            x = x*x
        return ans if n > 0 else 1/ans
                
                
