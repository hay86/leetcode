class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ret = ''
        f = 1
        for i in range(1, n+1):
            f *= i
        v = [False] * n
        for i in range(n, 0,-1):
            f /= i
            m = int((k-1)/f)
            k -= m*f
            j = 0
            while j < n:
                if not v[j]:
                    m -= 1
                    if m < 0:
                        break
                j += 1
            if j < n:
                ret += str(j+1)
                v[j] = True
        return ret
