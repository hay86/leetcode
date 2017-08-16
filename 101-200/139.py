class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if s == '':
            return True
        g = {}
        n = len(s)
        for w in wordDict:
            j = len(w)
            i = s.find(w)
            while i >= 0:
                if i not in g:
                    g[i] = set()
                g[i].add(i+j)
                i = s.find(w, i+1)
        q = [0]
        v = [False]*n
        v[0] = True
        while len(q) > 0:
            i = q.pop(0)
            if i in g:
                for j in g[i]:
                    if j == n:
                        i = n
                        break
                    if not v[j]:
                        q.append(j)
                        v[j] = True
            if i == n:
                break
        return i == n
