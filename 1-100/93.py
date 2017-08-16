class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        ret = []
        if size < 4 or size > 12:
            return ret
        s1 = 0
        for i in range(1, 4):
            s2 = s1 + i
            t1 = size - s2
            if t1 < 3 or t1 > 9 or s[s1] == '0' and i > 1:
                continue
            n1 = int(s[s1:s2])
            if n1 > 255:
                continue
            for j in range(1, 4):
                s3 = s2 + j
                t2 = size - s3
                if t2 < 2 or t2 > 6 or s[s2] == '0' and j > 1:
                    continue
                n2 = int(s[s2:s3])
                if n2 > 255:
                    continue
                for k in range(1, 4):
                    s4 = s3 + k
                    t3 = size - s4
                    if t3 < 1 or t3 > 3 or s[s3] == '0' and k > 1 or s[s4] == '0' and size-s4 > 1:
                        continue
                    n3 = int(s[s3:s4])
                    n4 = int(s[s4:])
                    if n3 > 255 or n4 > 255:
                        continue
                    ret.append("%d.%d.%d.%d" % (n1,n2,n3,n4))
        return ret
