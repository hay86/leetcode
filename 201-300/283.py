class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero == -1:
                    zero = i
            elif zero != -1 and zero != i:
                tmp = nums[zero]
                nums[zero] = nums[i]
                nums[i] = tmp
                zero += 1
