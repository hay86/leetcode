class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dp(n)
        
    def dp(self, n):
        if n == 1:
            return 1
        return 2*(n/2-self.dp(n/2)+1) 
