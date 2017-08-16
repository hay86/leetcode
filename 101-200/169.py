class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m, c = 0, 0
        for n in nums:
            if n != m:
                c -= 1
                if c <= 0:
                    c = 1
                    m = n
            else:
                c += 1
        return m
        
