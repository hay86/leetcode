class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        a, b = numerator, denominator
        sign = '-' if a*b < 0 else ''
        a = -a if a < 0 else a
        b = -b if b < 0 else b
        if b == 0:
            return 'NaN'
        elif a%b == 0:
            return sign + str(a/b)
        ret = sign + (str(a/b)+'.' if a > b else '0.')
        a = a%b
        m = {}
        i = len(ret)
        while True:
            m[a] = i
            a *= 10
            if a%b == 0:
                ret += str(a/b)
                break
            ret += (str(a/b) if a > b else '0')
            a = a%b
            if a in m:
                ret = ret[:m[a]] + '(' + ret[m[a]:] + ')'
                break
            i += 1
        return ret
