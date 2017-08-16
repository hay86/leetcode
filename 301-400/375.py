class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = [[2147483647]*(n+1) for i in range(n+1)]
        for i in range(1,n+1):
            ret[i][i] = 0
        for i in range(1,n):
            for j in range(1,n-i+1):
                s,e = j, i+j
                ret[s][e] = min(ret[s][e], s+ret[s+1][e], e+ret[s][e-1])
                for k in range(s+1,e):
                    ret[s][e] = min(ret[s][e], k+max(ret[s][k-1],ret[k+1][e]))
        return ret[1][n]
        
