class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sec_height = 0
        left = 0
        right = len(height)-1
        ret = 0
		
        while left < right:
            if height[left] < height[right]:
                sec_height = max(height[left], sec_height)
                ret += sec_height - height[left]
                left += 1
            else:
                sec_height = max(height[right], sec_height)
                ret += sec_height - height[right];
                right -= 1

        return ret
            
