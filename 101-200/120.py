class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        a = triangle[0]
        b = []
        n = len(triangle)
        for i in range(1, n):
            m = len(triangle[i])
            b.append(a[0]+triangle[i][0])
            for j in range(1,m-1):
                b.append(min(a[j-1]+triangle[i][j],a[j]+triangle[i][j]))
            b.append(a[-1] + triangle[i][-1])
            a = b
            b = []
        return min(a)
