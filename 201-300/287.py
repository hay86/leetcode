class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)-1
        l, r = 1, n
        while l <= r:
            m = (l+r)/2
            gt, lt = 0, 0
            for x in nums:
                if x > m:
                    gt += 1
                elif x < m:
                    lt += 1
            if lt > m-1:
                r = m-1
            elif gt > n-m:
                l = m+1
            else:
                break
        return m
