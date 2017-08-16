import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        s1 = len(self.minheap)
        s2 = len(self.maxheap)
        if s1 == s2:
            if s1 > 0 and self.minheap[0] >= num:
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        elif s1 > s2:
            if self.minheap[0] < num:
                heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, num)
            else:
                heapq.heappush(self.maxheap, -num)
        else:
            if self.maxheap[0] < -num:
                heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
                
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        s1 = len(self.minheap)
        s2 = len(self.maxheap)
        if s1 == s2:
            return (self.minheap[0]-self.maxheap[0])/2.
        else:
            return self.minheap[0] if s1 > s2 else -self.maxheap[0]

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
