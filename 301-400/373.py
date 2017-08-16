from heapq import heappush, heappop
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        ret = []
        if len(nums1) == 0 or len(nums2) == 0:
            return ret
        que = [(nums1[0]+nums2[0], 0, 0)]
        vis = set([(0,0)])
        for i in range(k):
            if len(que) == 0:
                break
            a, b, c = heappop(que)
            ret.append((nums1[b], nums2[c]))
            if b+1 < len(nums1) and (b+1,c) not in vis:
                vis.add((b+1,c))
                heappush(que, (nums1[b+1]+nums2[c], b+1, c))
            if c+1 < len(nums2) and (b,c+1) not in vis:
                vis.add((b,c+1))
                heappush(que, (nums1[b]+nums2[c+1], b, c+1))
        return ret
