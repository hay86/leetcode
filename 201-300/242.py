class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = [0]*26
        b = ord('a')
        for x in s:
            m[ord(x)-b] += 1
        for x in t:
            m[ord(x)-b] -= 1
        for x in m:
            if x != 0:
                return False
        return True
