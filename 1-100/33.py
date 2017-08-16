class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l<=r:
            m = int((l+r)/2)
            if target == nums[m]:
                return m
            elif nums[l] <= target < nums[m] or nums[l] > nums[m] and (nums[l] <= target or nums[m] > target):
                r = m-1
            elif nums[m] < target <= nums[r] or nums[r] < nums[m] and (target <= nums[r] or target > nums[m]):
                l = m+1
            else:
                break
        return -1
