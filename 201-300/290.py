class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str):
            return False
        d1, d2 = {}, {}
        size = len(pattern)
        for i in range(size):
            if str[i] not in d1:
                d1[str[i]] = pattern[i]
            elif d1[str[i]] != pattern[i]:
                return False
            if pattern[i] not in d2:
                d2[pattern[i]] = str[i]
            elif d2[pattern[i]] != str[i]:
                return False
        return True
