class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x+y < z:
            return False
        if z <= 0 :
            return True
        a,b = (x,y) if x>y else (y,x)
        while b>0:
            a,b = b,a%b
        return z%a == 0
