# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n == 0:
            return intervals
        intervals.sort(key=lambda x:x.start)
        ret = [intervals[0]]
        for i in range(1, n):
            if intervals[i].start > ret[-1].end:
                ret.append(intervals[i])
            elif intervals[i].end > ret[-1].end:
                ret[-1].end = intervals[i].end
        return ret
