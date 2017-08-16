class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        map = {}
        size = len(nums)
        for i in range(size):
            if nums[i] not in map or i - map[nums[i]] > k:
                map[nums[i]] = i
            else:
                return True
        return False
