class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stk = []
        n = len(nums)
        ak = float('-inf')
        for i in range(n-1, -1, -1):
            if nums[i] < ak:
                return True
            while len(stk) > 0 and stk[-1] < nums[i]:
                ak = stk.pop()
            stk.append(nums[i])
        return False