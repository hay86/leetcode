class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b,c = -2147483649, -2147483649, -2147483649
        for n in nums:
            if n == a or n == b or n == c:
                continue
            elif n > a:
                a,b,c = n,a,b
            elif n > b:
                a,b,c = a,n,b
            elif n > c:
                a,b,c = a,b,n
        return c if c > -2147483649 else a
