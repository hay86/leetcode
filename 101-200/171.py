class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        base = ord('A') - 1
        for x in s:
            ret = ret*26 + ord(x) - base
        return ret
