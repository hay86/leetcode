import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = []
        size = len(buildings)
        if size == 0:
            return ret
        buildings.append((2147483648,2147483648,0))
        heap = []
        heapq.heappush(heap, (-buildings[0][2],buildings[0][0],buildings[0][1]))
        s = heap[0][1]
        for i in range(1, size+1):
            b = buildings[i]
            last = None
            while len(heap) > 0 and b[0] >= heap[0][2]:
                if heap[0][2] > s:
                    if len(ret) == 0 or -heap[0][0] != ret[-1][1]:
                        if len(ret) > 0 and ret[-1][0] == s and ret[-1][1] < -heap[0][0]:
                            ret.pop()
                        ret.append((s, -heap[0][0]))
                    s = heap[0][2]
                last = heapq.heappop(heap)
            if len(heap) == 0:
                if last is not None and b[0] > last[2]:
                    ret.append((s, 0))
                    s = b[0]
            elif heap[0][1] < b[0] < heap[0][2]:
                if len(ret) == 0 or -heap[0][0] != ret[-1][1]:
                    if len(ret) > 0 and ret[-1][0] == s and ret[-1][1] < -heap[0][0]:
                        ret.pop()
                    ret.append((s, -heap[0][0]))
                s = b[0]
            heapq.heappush(heap, (-b[2],b[0],b[1]))
        return ret
