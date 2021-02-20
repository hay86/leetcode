# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        n = len(intervals)
        if n == 0:
            return []
        ret = [-1]*n
        start = [(e.start, i) for i,e in enumerate(intervals)]
        end = [(e.end, i) for i,e in enumerate(intervals)]
        start.sort()
        end.sort()
        i, j = 0, 0
        while i<n and j<n:
            if end[j][0] <= start[i][0]:
                ret[end[j][1]] = start[i][1]
                j += 1
            else:
                i += 1
        return ret
