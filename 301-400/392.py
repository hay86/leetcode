class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        for c in s:
            p = t.find(c,i)
            if p == -1:
                return False
            else:
                i = p + 1
        return True
