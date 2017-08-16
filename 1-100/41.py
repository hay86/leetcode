class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 1
        for i in range(size):
            v = nums[i]
            while 0 < v <= size and nums[v-1] != v:
                tmp = nums[v-1]
                nums[v-1] = v
                v = tmp
        for i in range(size):
            if nums[i] != i+1:
                return i+1
        return i+2
