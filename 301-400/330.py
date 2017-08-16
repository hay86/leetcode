class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        ret = 0
        total = 0
        i = 0
        while i < len(nums) and total < n:
            need = total+1
            if nums[i] > need:
                ret += 1
                total += need
            else:
                total += nums[i]
                i += 1
        while total < n:
            total = total*2+1
            ret += 1
        return ret
