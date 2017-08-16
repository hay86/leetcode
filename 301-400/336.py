class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        m = {w:i for i, w in enumerate(words)}
        ret = set()
        for i, w in enumerate(words):
            for j in range(0, len(w)+1):
                a = w[:j]
                b = w[j:]
                if a == a[::-1]:
                    if b[::-1] in m:
                        j = m[b[::-1]]
                        if i != j:
                            ret.add((j, i))
                if b == b[::-1]:
                    if a[::-1] in m:
                        j = m[a[::-1]]
                        if i != j:
                            ret.add((i, j))
        return list(ret)
