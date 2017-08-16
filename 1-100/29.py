class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend < 0:
            sign = 0-sign
            dividend = 0-dividend
        if divisor < 0:
            sign = 0-sign
            divisor = 0-divisor
        if divisor == 0:
            return -1
        if dividend < divisor:
            return 0
        ret = 0
        while dividend >= divisor:
            c, d = 0, divisor
            while d <= dividend:
                d <<= 1
                c += 1
            dividend -= (d>>1)
            ret += 2**(c-1)
        if sign == 1:
            return ret if ret <= 2147483647 else 2147483647
        else:
            ret = 0-ret
            return ret if ret >= -2147483648 else -2147483648
