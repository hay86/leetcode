class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num > 0:
            prime = [2,3,5]
            for p in prime:
                while num % p == 0:
                    num = num / p
        return num == 1
