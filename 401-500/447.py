class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ret = 0
        for p in points:
            m = {}
            for q in points:
                d = (p[0]-q[0])**2 + (p[1]-q[1])**2
                m[d] = m.get(d, 0) + 1
            for c in m.values():
                if c > 1:
                    ret += c*(c-1)
        return ret