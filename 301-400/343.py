class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        for i in range(2, n+1):
            d = n % i
            if d == 0:
                j = (n/i)**i
            else:
                j = (n/i+1)**d * (n/i)**(i-d)
            if j > ret:
                ret = j
            else:
                break
        return ret
        
