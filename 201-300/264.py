class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(n-1):
            m2, m3, m5 = q[i2]*2, q[i3]*3, q[i5]*5
            m = min(m2, m3, m5)
            if m2 == m:
                i2 += 1
            if m3 == m:
                i3 += 1
            if m5 == m:
                i5 += 1
            q.append(m)
        return q[-1]
