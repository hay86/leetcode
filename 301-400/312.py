class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = {}
        nums.insert(0,1)
        nums.append(1)
        return self.div(nums, 0, len(nums)-1, cache)
        
    def div(self, nums, s, e, cache):
        if (s, e) in cache:
            return cache[(s, e)]
        v = 0
        for i in range(s+1, e):
            if (s, i) in cache:
                v1 = cache[(s, i)]
            else:
                v1 = self.div(nums, s, i, cache)
                cache[(s, i)] = v1
            if (i, e) in cache:
                v2 = cache[(i, e)]
            else:
                v2  = self.div(nums, i, e, cache)
                cache[(i, e)] = v2
            if v1 + v2 + nums[s]*nums[i]*nums[e] > v:
                v = v1 + v2 + nums[s]*nums[i]*nums[e]
        return v
