class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size == 0:
            return 0
        m = {}
        ret, tmp, start = 0, 0, 0
        for i in range(size):
            if s[i] in m and m[s[i]]+1 > start:
                tmp -= m[s[i]] - start
                start = m[s[i]]+1
            else:
                tmp += 1
            m[s[i]] = i
            if tmp > ret:
                ret = tmp
        return ret
