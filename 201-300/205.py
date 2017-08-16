class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        size = len(s)
        for i in range(size):
            if t[i] not in d1:
                d1[t[i]] = s[i]
            elif d1[t[i]] != s[i]:
                return False
            if s[i] not in d2:
                d2[s[i]] = t[i]
            elif d2[s[i]] != t[i]:
                return False
        return True
