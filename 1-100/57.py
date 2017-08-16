# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]
        if intervals[0].start >= newInterval.start:
            intervals.insert(0, newInterval)
        elif intervals[-1].start <= newInterval.start:
            intervals.append(newInterval)
        else:
            s, e = 0, len(intervals)-1
            while s <= e:
                m = int((s+e)/2)
                if intervals[m].start < newInterval.start:
                    s = m+1
                else:
                    e = m-1
            intervals.insert(s, newInterval)
        ret = []
        i, j = 1, intervals[0]
        while i < len(intervals):
            if j.end < intervals[i].start:
                ret.append(j)
                j = intervals[i]
            elif j.end < intervals[i].end:
                j.end = intervals[i].end
            i += 1
        ret.append(j)
        return ret
