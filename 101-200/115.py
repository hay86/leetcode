class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        ss = len(s)
        st = len(t)
        m = [[0]*(ss+1) for i in range(st+1)]
        for i in range(ss+1):
            m[0][i] = 1
        for i in range(st):
            for j in range(ss):
                m[i+1][j+1] = m[i+1][j]
                if s[j] == t[i]:
                    m[i+1][j+1] += m[i][j]
        return m[st][ss]
