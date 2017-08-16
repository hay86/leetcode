class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        tmp = 1
        for x in nums:
            ret.append(tmp)
            tmp *= x
        tmp = 1
        for i in range(len(ret)):
            ret[-i-1] *= tmp
            tmp *= nums[-i-1]
        return ret
            
