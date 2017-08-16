class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size <= 2:
            return size
        j = 1
        for i in range(2,size):
            if nums[i] != nums[j] or nums[i] != nums[j-1]:
                j += 1
                if i != j:
                    nums[j] = nums[i]
        return j+1
