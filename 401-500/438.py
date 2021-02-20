class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n,m = len(p),len(s)
        if m < n:
            return []
        target = [0]*26
        value = [0]*26
        for i in range(n):
            target[ord(p[i])-97] += 1
            value[ord(s[i])-97] += 1
        ret = []
        if target == value:
            ret.append(0)
        for i in range(n, m):
            value[ord(s[i])-97] += 1
            value[ord(s[i-n])-97] -= 1
            if target == value:
                ret.append(i-n+1)
        return ret
