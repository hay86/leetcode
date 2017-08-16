class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        size1 = len(s1)
        size2 = len(s2)
        if size1 == 0:
            return s2 == s3
        if size2 == 0:
            return s1 == s3
        if len(s3) != size1+size2:
            return False
        m = [[False]*(size1+1) for i in range(size2+1)]
        m[0][0] = True
        for i in range(1, size1+1):
            m[0][i] = m[0][i-1] and s1[i-1] == s3[i-1]
        for i in range(1, size2+1):
            m[i][0] = m[i-1][0] and s2[i-1] == s3[i-1]
        for i in range(1, size2+1):
            for j in range(1, size1+1):
                m[i][j] = m[i-1][j] and s2[i-1] == s3[i+j-1] or m[i][j-1] and s1[j-1] == s3[i+j-1]
        return m[size2][size1]
