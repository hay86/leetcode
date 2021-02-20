class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ret = 0
        dp = [{}]
        for i in range(1, len(A)):
            dpi = {}
            for j in range(i):
                d = A[i] - A[j]
                r3, r2 = dpi.get(d, (0, 0))
                if d in dp[j]:
                    k = sum(dp[j][d])
                    dpi[d] = (r3 + k, r2 + 1)
                    ret += k
                else:
                    dpi[d] = (r3, r2 + 1)
            dp.append(dpi)
        return ret
