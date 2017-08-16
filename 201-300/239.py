class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = []
        ret = []
        size = len(nums)
        for i in range(size):
            while len(q) > 0 and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
            if i >= k-1:
                while q[0][1] <= i-k:
                    q.pop(0)
                ret.append(q[0][0])
        return ret
