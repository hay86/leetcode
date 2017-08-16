class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[0]*33
        for x in nums:
            c = 0
            y = abs(x)
            while y > 0:
                if y&1 == 1:
                    a[c] = (a[c] + 1) % 3
                y = y>>1
                c += 1
            if x < 0:
                a[32] = (a[32] + 1) % 3
        ret = 0
        for i in range(32):
            ret = ret*2 + a[-i-2]
        return ret if a[32] == 0 else -ret
