class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = len(nums)
        if s == 0:
            return 0
        ret = [0]*(target+1)
        for i in range(1,target+1):
            for j in range(s):
                if nums[j] == i:
                    ret[i] += 1
                elif nums[j] < i:
                    ret[i] += ret[i-nums[j]]
        return ret[target]
        
