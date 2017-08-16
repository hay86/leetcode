class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        nums.append(2147483647)
        size = len(nums)
        s, t = nums[0], 0
        ret = []
        for i in range(1, size):
            k = nums[i]
            if k-s != i-t:
                j = nums[i-1]
                if s != j:
                    ret.append('%d->%d' % (s,j))
                else:
                    ret.append('%d' % j)
                s, t = k, i
        return ret
