class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        size = len(citations)
        l, r = 0, size-1
        ret = 0
        while l<=r:
            m = int((l+r)/2)
            if citations[m] >= size-m:
                ret = size-m
                r = m-1
            else:
                l = m+1
        return ret
