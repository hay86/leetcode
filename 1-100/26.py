class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        j = 0
        for i in range(1,size):
            if nums[i] > nums[j]:
                j += 1
                if i != j:
                    nums[j] = nums[i]
        return j+1
