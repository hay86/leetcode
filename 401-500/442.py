class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for n in nums:
            if n < 0:
                n = -n
            if nums[n-1] < 0:
                r.append(n)
            else:
                nums[n-1] = -nums[n-1]
        return r