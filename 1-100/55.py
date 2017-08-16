class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_true = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > 0 and i+nums[i] >= last_true:
                last_true = i
        return last_true == 0
