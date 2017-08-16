class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        contain = [0]*size
        not_contain = [0]*size
        contain[0] = nums[0]
        for i in range(1,size):
            contain[i] = not_contain[i-1]+nums[i]
            not_contain[i] = max(contain[i-1], not_contain[i-1])
        return max(contain[size-1],not_contain[size-1])
