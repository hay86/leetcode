class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret=[-1]*26
        for i in range(len(s)):
            v = ord(s[i]) - 97
            if ret[v] >= 0:
                ret[v] = -2
            elif ret[v] == -1:
                ret[v] = i
        v = -1
        for r in ret:
            if r >= 0 and (r < v or v == -1):
                v = r
        return v
