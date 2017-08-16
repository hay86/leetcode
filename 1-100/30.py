class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ret = []
        s1 = len(words)
        s2 = len(s)
        if s1 == 0:
            return ret
        s3 = len(words[0])
        m = {}
        p = []
        for i in range(s2-s3+1):
            sub = s[i:i+s3]
            for w in words:
                if sub == w:
                    m[i] = w
                    p.append(i)
                    break
        m2 = {}
        for w in words:
            m2[w] = m2[w]+1 if w in m2 else 1
        for i in p:
            if s2-i < s1*s3:
                break
            m3 = {}
            j, k = 0, s1*s3
            while j < k:
                if (i+j) in m:
                    x = m[i+j]
                    if x not in m3:
                        m3[x] = 1
                    elif m3[x] < m2[x]:
                        m3[x] += 1
                    else:
                        break
                else:
                    break
                j += s3
            if j >= k:
                ret.append(i)
        return ret
