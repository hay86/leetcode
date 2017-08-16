class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        a = [0]
        for i in range(n):
            start = len(a)-1
            for j in range(start,-1,-1):
                a.append(a[j]|(1<<i))
        return a
