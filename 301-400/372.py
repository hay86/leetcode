class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        x = 1337
        a %= x
        ret = 1
        while len(b) > 0:
            if b[-1] > 0:
                ret = (ret * pow(a, b[-1], x)) % x
            a = pow(a, 10, x)
            b.pop()
        return ret
