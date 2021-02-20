# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x:x.end)
        far = -2147483648
        ret = 0
        for x in intervals:
            if x.start >= far:
                far = x.end
            else:
                ret += 1
        return ret
