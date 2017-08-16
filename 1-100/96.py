class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0] * (n+1)
        a[1] = 1
        for i in range(2, n+1):
            a[i] += 2*a[i-1]
            for j in range(1, i-1):
                a[i] += a[j] * a[i-j-1]
        return a[n]
