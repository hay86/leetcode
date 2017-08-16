class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 4:
            return False
        else:
            sum = 0
            while n > 0:
                sum += (n%10)**2
                n = int(n/10)
            return self.isHappy(sum)
