class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = {}
        for x in nums:
            if x not in m:
                m[x] = True
            else:
                return True
        return False
