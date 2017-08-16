class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, tmp = nums[0], 0
        for x in nums:
            tmp += x
            if tmp > ret:
                ret = tmp
            if tmp < 0:
                tmp = 0

        return ret
