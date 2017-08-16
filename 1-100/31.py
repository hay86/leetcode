class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size <= 1:
            return
        i = size-2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        if i >= 0:
            j = i+1
            while j < size:
                if nums[j] <= nums[i]:
                    tmp = nums[i]
                    nums[i] = nums[j-1]
                    nums[j-1] = tmp
                    break
                j += 1
            if j == size:
                tmp = nums[i]
                nums[i] = nums[j-1]
                nums[j-1] = tmp
        n = int((size-i-1)/2)
        for j in range(n):
            tmp = nums[i+1+j]
            nums[i+1+j] = nums[-j-1]
            nums[-j-1] = tmp
            
