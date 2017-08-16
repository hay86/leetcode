class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        m, n = {}, len(s)
        for word in wordDict:
            j = len(word)
            i = s.find(word)
            while i != -1:
                if i not in m:
                    m[i] = set()
                m[i].add(i+j)
                i = s.find(word, i+1)
        q = [0]
        v = [False]*n
        v[0] = True
        while len(q) > 0:
            i = q.pop(0)
            if i in m:
                for j in m[i]:
                    if j == n:
                        i = n
                        break
                    if not v[j]:
                        q.append(j)
                        v[j] = True
            if i == n:
                break
        ret = []
        if i == n:
            self.dfs(0, s, m, [], ret)
        return ret
        
    def dfs(self, i, s, m, path, ret):
        if len(s) == i:
            ret.append(' '.join(path))
        elif i in m:
            for j in m[i]:
                path.append(s[i:j])
                self.dfs(j, s, m, path, ret)
                path.pop()
        
