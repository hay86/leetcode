class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = 0
        zero = False
        for x in nums:
            sum += x
            if x > max:
                max = x
            if x == 0:
                zero = True
        x = (max+1)*max/2-sum
        return 0 if not zero else (max+1 if x == 0 else x)
