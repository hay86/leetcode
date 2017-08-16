class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        size = len(nums)
        ret = []
        for i in range(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = size-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif sum > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return ret
