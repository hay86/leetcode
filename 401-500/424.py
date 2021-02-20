class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        arr = set(list(s))
        ans = 0
        for a in arr:
            i, j, c = -1, 0, 0
            while j < len(s):
                if s[j] != a:
                    c += 1
                if c > k:
                    i += 1
                    while s[i] == a:
                        i += 1
                    c -= 1
                ans = max(ans, j-i)
                j += 1
        return ans
