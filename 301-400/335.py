class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        size = len(x)
        for i in range(3, size):
            if x[i-3] >= x[i-1] and x[i] >= x[i-2]:
                return True
            if i>3 and x[i-1] == x[i-3] and 0 <= x[i-2]-x[i-4] <= x[i]:
                return True
            if i>4 and 0 <= x[i-3]-x[i-1] <= x[i-5] and 0 <= x[i-2]-x[i-4] <= x[i]:
                return True
        return False
