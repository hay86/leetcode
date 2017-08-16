class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            k = (l+r)/2
            if nums[l]<=nums[k]<=nums[r]:
                r = l
            elif nums[l]<=nums[k]:
                l = k+1
            else:
                r = k
        return nums[l]
            
