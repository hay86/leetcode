class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    	l, r = 0, len(nums)-1
    	while l <= r:
    		m = int((l+r)/2)
    		if (m-1 < 0 or nums[m-1] < nums[m]) and (m+1 > len(nums)-1 or nums[m+1] < nums[m]):
    			return m
    		if l < m and nums[m] <= nums[l] or m-1 >= 0 and nums[m] < nums[m-1]:
    			r = m-1
    		else:
    			l = m+1
