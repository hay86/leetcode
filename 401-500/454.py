class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        v = {}
        for a in A:
            for b in B:
                v[a+b] = v.get(a+b, 0) + 1
        ans = 0
        for c in C:
            for d in D:
                if -c-d in v:
                    ans += v[-c-d]
        return ans