class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        height.append(0)
        stack = []
        size = len(height)
        ret = 0
        for i in range(size):
            while len(stack) > 0 and height[stack[-1]] > height[i]:
                j = stack.pop()
                k = -1 if len(stack) == 0 else stack[-1]
                ret = max(ret, height[j]*(i-k-1))
            stack.append(i)
        return ret
