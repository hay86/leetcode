class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        size = len(s)
        for i in range(size-1, -1, -1):
            if s[i] != ' ':
                ret += 1
            elif ret > 0:
                break
        return ret
