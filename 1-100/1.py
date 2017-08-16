class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        s = len(nums)
        for i in range(s-1,-1,-1):
            v1 = nums[i]
            v2 = target - v1
            if v2 in m:
                return [i+1,m[v2]+1]
            else:
                m[v1] = i
        return [-1, -1]
