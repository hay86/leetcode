class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 0:
            return 0
        dp = [1]*size
        q = [0]*(size+1)
        q[1] = nums[0]
        qm = 1
        for i in range(1,size):
            l,r = 1,qm
            while l<=r:
                m = int((l+r)/2)
                if q[m] >= nums[i]:
                    r = m-1
                else:
                    l = m+1
            dp[i] = r+1
            q[dp[i]] = nums[i]
            if qm < dp[i]:
                qm = dp[i]
        return max(dp)
