class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        elif n % 2 == 1:
            x = (n-1)/2
            if x % 2 == 1 and x != 1:
                return self.integerReplacement((n+1)/2)+2
            else:
                return self.integerReplacement((n-1)/2)+2
        else:
            return self.integerReplacement(n/2)+1
