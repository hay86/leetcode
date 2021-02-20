class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = [0]*255
        for c in s:
            ret[ord(c)] += 1
        ans, plus = 0, 0
        for c in ret:
            if c%2 == 0:
                ans += c
            else:
                ans += c-1
                plus = 1
        return ans+plus
