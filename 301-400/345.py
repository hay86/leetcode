class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        o = ['a','e','i','o','u','A','E','I','O','U']
        i, j = 0, len(s)-1
        while i < j:
            while i < j and s[i] not in o:
                i += 1
            while i < j and s[j] not in o:
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i, j = i+1, j-1
        return ''.join(s)
