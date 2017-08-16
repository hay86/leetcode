class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret=[0]*(num+1)
        j, k = 0, 1
        for i in range(1, num+1):
            ret[i] = ret[i&j] + 1
            if i == k:
                j, k = k, (k<<1)+1
        return ret
