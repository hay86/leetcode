class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = len(chars)
        if s <= 1:
            return s
        p,c = 1,1
        for i in range(1, s):
            if chars[i] == chars[i-1]:
                c += 1
            else:
                if c > 1:
                    for d in str(c):
                        chars[p] = d
                        p += 1
                chars[p] = chars[i]
                p += 1
                c = 1
        if c > 1:
            for d in str(c):
                chars[p] = d
                p += 1
        return p