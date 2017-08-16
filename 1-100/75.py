class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        firstW, firstB = -1, -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if firstW == -1:
                    firstW = i
                if firstB != -1:
                    nums[firstB] = 1
                    if firstW > firstB:
                        firstW = firstB
                    nums[i] = 2
                    firstB += 1
            elif nums[i] == 2:
                if firstB == -1:
                    firstB = i
            else:
                if firstW != -1:
                    nums[firstW] = 0
                    if firstB != -1:
                        nums[firstB] = 1
                        nums[i] = 2
                        firstB += 1
                    else:
                        nums[i] = 1 
                    firstW += 1
                elif firstB != -1:
                    nums[firstB] = 0
                    nums[i] = 2
                    firstB += 1
