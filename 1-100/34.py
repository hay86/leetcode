class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(nums)-1
        while l<=r:
            m = int((l+r)/2)
            if nums[m] >= target:
                r = m-1
            else:
                l = m+1
        left = -1 if r+1 >= len(nums) or nums[r+1] != target else r+1
        l, r = 0, len(nums)-1
        while l<=r:
            m = int((l+r)/2)
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
        right = -1 if l-1 < 0 or nums[l-1] != target else l-1
        return [left, right]
