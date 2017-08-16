class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = len(nums)
        if s < 2:
            return nums
        nums.sort()
        size = [0]*s
        prev = [x for x in range(s)]
        ms, mp = 0, 0
        for i in range(1,s):
            for j in range(i):
                if nums[i] % nums[j] == 0 and size[i] < size[j]+1:
                    size[i] = size[j]+1
                    prev[i] = j
                    if ms < size[i]:
                        ms = size[i]
                        mp = i
        ret = []
        while True:
            ret.append(nums[mp])
            if mp == prev[mp]:
                break
            mp = prev[mp]
        ret.reverse()
        return ret
