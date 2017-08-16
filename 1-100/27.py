class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = len(nums)-1
        while i>=0 and nums[i] == val:
            i -= 1
        j = 0
        while j < i:
            if nums[j] == val:
                nums[j] = nums[i]
                nums[i] = val
                while i>=0 and nums[i] == val:
                    i -= 1
            j += 1
        return i+1
