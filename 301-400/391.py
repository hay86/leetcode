class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        corner = set()
        xmin, ymin = 2147483647, 2147483647
        xmax, ymax = -2147483648, -2147483648
        area = 0
        for r in rectangles:
            xmin, ymin = min(xmin, r[0]), min(ymin, r[1])
            xmax, ymax = max(xmax, r[2]), max(ymax, r[3])
            area += (r[2]-r[0])*(r[3]-r[1])
            for s in [(r[0],r[1]),(r[2],r[3]),(r[0],r[3]),(r[2],r[1])]:
                if s in corner:
                    corner.remove(s)
                else:
                    corner.add(s)
        return corner == set([(xmin,ymin),(xmin,ymax),(xmax,ymin),(xmax,ymax)]) and area == (xmax-xmin)*(ymax-ymin)
