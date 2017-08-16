# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.father = {}
        self.num = set()
        
    def getFather(self, val):
        if val != self.father[val]:
            self.father[val] = self.getFather(self.father[val])
        return self.father[val]

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.father:
            return
        self.father[val] = val
        self.num.add(val)
        if val-1 in self.father:
            f = self.getFather(val-1)
            if f < val:
                self.father[val] = f
            else:
                self.father[f] = val
        if val+1 in self.father:
            f = self.getFather(val+1)
            if f < val:
                self.father[val] = f
            else:
                self.father[f] = val

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        ret = {}
        rm = []
        for v in self.num:
            f = self.getFather(v)
            if f not in ret:
                ret[f] = v
            else:
                rm.append(min(ret[f], v))
                ret[f] = max(ret[f], v)
        for v in rm:
            self.num.remove(v)
        ret = sorted(ret.items(), key=lambda x: x[0])
        return ret


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
