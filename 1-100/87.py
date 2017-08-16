class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        if sorted(list(s1)) != sorted(list(s2)):
            return False
        n = len(s1)
        for i in range(1,n):
            s11, s12 = s1[:i], s1[i:]
            s21, s22 = s2[:i], s2[i:]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
            s21, s22 = s2[-i:], s2[-n:-i]
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return True
        return False
