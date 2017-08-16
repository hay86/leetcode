class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        positive = nums[0]
        negative = nums[0]
        ret = nums[0]
        for i in range(1, size):
            tmp1 = max(nums[i], positive*nums[i], negative*nums[i])
            tmp2 = min(nums[i], positive*nums[i], negative*nums[i])
            positive, negative = tmp1, tmp2
            ret = max(ret, positive, negative)
        return ret
