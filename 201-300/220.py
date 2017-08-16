class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k == 0:
            return False
        size = len(nums)
        if size == 0:
            return False
        m = {}
        if t == 0:
            for i in range(size):
                if nums[i] not in m or i - m[nums[i]] > k:
                    m[nums[i]] = i
                else:
                    return True
            return False
        base = min(nums)
        for i in range(size):
            buck = (nums[i] - base) / t
            if buck-1 in m:
                for j in m[buck-1]:
                    if abs(i-j) <= k and abs(nums[i]-nums[j]) <= t:
                        return True
            if buck+1 in m:
                for j in m[buck+1]:
                    if abs(i-j) <= k and abs(nums[i]-nums[j]) <= t:
                        return True
            if buck in m:
                for j in m[buck]:
                    if abs(i-j) <= k and abs(nums[i]-nums[j]) <= t:
                        return True
                m[buck].append(i)
            else:
                m[buck] = [i]
        return False
