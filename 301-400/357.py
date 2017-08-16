class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [1,10]
        for i in range(10, 1, -1):
            ret.append((ret[-1]-ret[-2])*i+ret[-2])
        return ret[n] if n < len(ret) else ret[-1]
