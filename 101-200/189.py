class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k%size
        if k == 0:
            return
        nums[:k], nums[k:] = nums[-k:], nums[:-k]
