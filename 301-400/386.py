class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ret = []
        v = 1
        i = 1
        while i <= n:
            ret.append(v)
            if v*10 <= n:
                v *= 10
            elif v%10 != 9 and v+1 <= n:
                v += 1
            else:
                while (v/10)%10 == 9:
                    v /= 10
                v = v/10 + 1
            i += 1
        return ret
