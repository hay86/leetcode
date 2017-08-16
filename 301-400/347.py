class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = {}
        for n in nums:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        m = sorted(m.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in m[:k]]
