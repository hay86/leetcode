class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        size = len(nums)
        ret = 2**31-1
        for i in range(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = size-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(ret-target) > abs(sum-target):
                    ret = sum
                if sum == target:
                    break
                elif sum > target:
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
            if ret == target:
                break
        return ret
