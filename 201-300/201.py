class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ret = 0
        base = [0]
        for i in range(32):
            base.append(1<<i)
        for b in range(-1,-33,-1):
            if base[b-1] <= m and n < base[b]:
                ret += base[b-1]
                m -= base[b-1]
                n -= base[b-1]
            elif m < base[b-1] and n >= base[b-1]:
                break
        return ret
