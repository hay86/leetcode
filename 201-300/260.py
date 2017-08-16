class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = {}
        for x in nums:
            if x not in m:
                m[x] = True
            else:
                del m[x]
        return list(m)
