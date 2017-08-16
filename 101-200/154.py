class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min = nums[0]
        size = len(nums)
        for i in range(1,size):
            if nums[i] < min:
                min = nums[i]
        return min
