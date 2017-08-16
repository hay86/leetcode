class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        size = len(nums)
        if size < 3:
            return False
        i, j = 0, -1
        imin = 0
        for k in range(1, size):
            if j == -1:
                if nums[k] > nums[i]:
                    j = k
                else:
                    i = k
            else:
                if nums[k] > nums[j]:
                    return True
                elif nums[k] > nums[i]:
                    j = k
                elif nums[k] > nums[imin]:
                    i, j = imin, k
            if nums[k] < nums[imin]:
                imin = k
        return False
