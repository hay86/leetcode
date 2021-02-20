class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k = nums[len(nums)/2]
        ret = 0
        for n in nums:
            ret += abs(k-n)
        return ret