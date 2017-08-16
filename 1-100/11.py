class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        ret = -1
        while l<r:
            tmp = (r-l)*min(height[r],height[l])
            if tmp > ret:
                ret = tmp
            if height[r] < height[l]:
                h = height[r]
                while l<r:
                    r -= 1
                    if height[r] >= h:
                        break
            else:
                h = height[l]
                while l<r:
                    l += 1
                    if height[l] >= h:
                        break
        return ret
