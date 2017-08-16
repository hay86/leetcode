class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m = {}
        size = len(nums)
        ret = set()
        for i in range(size-1):
            for j in range(i+1, size):
                v = nums[i]+nums[j]
                if v not in m:
                    m[v] = set()
                m[v].add((i,j))
        for k,v in m.items():
            k2 = target - k
            if k2 in m:
                v2 = m[k2]
                for vv in v:
                    for vv2 in v2:
                        if vv[0] != vv2[0] and vv[1] != vv2[0] and vv[0] != vv2[1] and vv[1] != vv2[1]:
                            ret.add(tuple(sorted([nums[vv[0]],nums[vv[1]],nums[vv2[0]],nums[vv2[1]]])))
        return list(ret)
