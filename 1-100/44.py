class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        S = len(s)
        P = len(p)
        i, j, star_i, star_j = 0, 0, -1, -1
        while i < S and j < P:
            if s[i] == p[j] or p[j] == '?':
                i += 1
                j += 1
            elif p[j] == '*':
                star_i, star_j = i, j
                j += 1
            elif star_i != -1:
                i, j = star_i + 1, star_j + 1
                star_i += 1
            else:
                return False
            if i < S and j == P:
                if star_i != -1:
                    i, j = star_i + 1, star_j + 1
                    star_i += 1
                else:
                    return False
        if i < S:
            return P > 0 and p[-1] == '*'
        if j < P:
            while j < P and p[j] == '*':
                j += 1
            return j == P
        return True
