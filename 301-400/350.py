class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m1, m2 = {}, {}
        for n in nums1:
            if n in m1:
                m1[n] += 1
            else:
                m1[n] = 1
        for n in nums2:
            if n in m2:
                m2[n] += 1
            else:
                m2[n] = 1
        
        ret = []
        keys = set(nums1) & set(nums2)
        
        for k in keys:
            ret += [k] * min(m1[k], m2[k])
        return ret
