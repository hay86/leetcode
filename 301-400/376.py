class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = len(nums)
        if s == 0:
            return 0
        pos, neg = [(1,nums[0])]*s, [(1,nums[0])]*s
        for i in range(1, s):
            p1,p2 = pos[i-1]
            n1,n2 = neg[i-1]
            if p1%2 == 1:
                pos[i] = (p1+1, nums[i]) if nums[i] > p2 else (p1, nums[i])
            else:
                pos[i] = (p1+1, nums[i]) if nums[i] < p2 else (p1, nums[i])
            if n1%2 == 1:
                neg[i] = (n1+1, nums[i]) if nums[i] < n2 else (n1, nums[i])
            else:
                neg[i] = (n1+1, nums[i]) if nums[i] > n2 else (n1, nums[i])
        return max(pos[s-1][0], neg[s-1][0])
