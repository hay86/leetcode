class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        import time
        dp1 = self.dp(nums1, k)
        dp2 = self.dp(nums2, k)
        ret = ''
        if len(dp1) == k and dp1[-1] > ret:
            ret = dp1[-1]
        if len(dp2) == k and dp2[-1] > ret:
            ret = dp2[-1]
        for i in range(k-1):
            j = k-i-2
            if len(dp1) > i and len(dp2) > j:
                ret = max(ret, self.dp2(dp1[i], dp2[j]))
        return [int(x) for x in list(ret)]
        
    def dp(self, nums, k):
        size = len(nums)
        if size == 0:
            return []
        prev, next = [str(nums[0])], ['' for i in range(size)]
        for i in range(1, size):
            prev.append(max(str(nums[i]), prev[-1]))
        ret = [prev[-1]]
        for i in range(2, min(size, k)+1):
            for j in range(i-1, size):
                next[j] = max(next[j-1], prev[j-1]+str(nums[j]))
            prev, next = next, ['' for i in range(size)]
            ret.append(prev[-1])
        return ret
        
    def dp2(self, d1, d2):
        ret, i1, i2, s1, s2 = '', 0, 0, len(d1), len(d2)
        while i1 < s1 and i2 < s2:
            if d1[i1] > d2[i2]:
                ret += d1[i1]
                i1 += 1
            elif d1[i1] < d2[i2]:
                ret += d2[i2]
                i2 += 1
            else:
                j1, j2 = i1+1, i2+1
                while j1 < s1 and j2 < s2 and d1[j1] == d2[j2]:
                    j1 += 1
                    j2 += 1
                if j1 == s1 or j2 < s2 and d1[j1] < d2[j2]:
                    ret += d2[i2]
                    i2 += 1
                else:
                    ret += d1[i1]
                    i1 += 1
        if i1 < s1:
            ret += d1[i1:]
        if i2 < s2:
            ret += d2[i2:]
        return ret  
