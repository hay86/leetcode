class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        prefix = 1
        k -= 1
        while k > 0:
            j = self.num(prefix, n)
            if k >= j:
                prefix += 1
                k -= j
            else:
                prefix *= 10
                k -= 1
        return prefix

    def num(self, prefix, n):
        ret, exp = 0, 0
        m = prefix
        while m <= n:
            ret += min(n - m + 1, 10 ** exp)
            m *= 10
            exp += 1
        return ret
