class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        sizeA = len(A)
        if sizeA == 0:
            return 0
        ret, x, y = -2147483648, 0, 0
        for i, a in enumerate(A):
            x += i*a
            y += a
        for a in A:
            x = x-y+sizeA*a
            ret = max(ret, x)
        return ret
