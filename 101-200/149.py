# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        size = len(points)
        if size == 0:
            return 0
        points.sort(key=lambda x:(x.x,x.y))
        n = []
        for p in points:
            if len(n) == 0 or n[-1][0] != p.x or n[-1][1] != p.y:
                n.append([p.x, p.y, 1])
            else:
                n[-1][2] += 1
        m = {}
        size = len(n)
        if size == 1:
            return n[0][2]
        for i in range(size):
            x1, y1, c1 = n[i]
            for j in range(i+1, size):
                x2, y2, c2 = n[j]
                a = (y1-y2+.0)/(x1-x2) if x1-x2 != 0 else 1
                b = -1 if x1-x2 != 0 else 0
                c = (x1*y2-x2*y1+.0)/(x1-x2) if x1-x2 != 0 else -x1
                if (a,b,c) in m:
                    m[(a,b,c)].add((x1, y1, c1))
                    m[(a,b,c)].add((x2, y2, c2))
                else:
                    m[(a,b,c)] = set([(x1, y1, c1),(x2, y2, c2)])
        ret = 0
        for s in m.values():
            ret = max(ret, sum([x[2] for x in s]))
        return ret
        
