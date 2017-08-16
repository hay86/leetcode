class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1 == word2:
            return 0
        ret = [[0]*(len(word1)+1) for i in range(len(word2)+1)]
        for i in range(1,len(word1)+1):
            ret[0][i] = i
        for i in range(1,len(word2)+1):
            ret[i][0] = i
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word1[j-1] == word2[i-1]:
                    ret[i][j] = min(ret[i-1][j]+1, ret[i][j-1]+1, ret[i-1][j-1])
                else:
                    ret[i][j] = min(ret[i-1][j]+1, ret[i][j-1]+1, ret[i-1][j-1]+1)
                    
        return ret[len(word2)][len(word1)]
