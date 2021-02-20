class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(2, len(s)+1):
            if len(s)%i == 0:
                if s[:len(s)/i]*i == s:
                    return True
        return False