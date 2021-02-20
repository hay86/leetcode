class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        ans, start = 0, 2**31
        for p in points[::-1]:
            if p[1] < start:
                ans += 1
                start = p[0]
        return ans