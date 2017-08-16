class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sizes = len(s)
        sizep = len(p)
        dp = [[False]*(sizes+1) for i in range(sizep+1)]
        dp[0][0] = True
        for i in range(1, sizep+1):
            dp[i][0] = dp[i-1][0] if i<sizep and p[i] == '*' or p[i-1] == '*' else False
            for j in range(1, sizes+1):
                if i<sizep and p[i] == '*':
                    if p[i-1] == s[j-1] or p[i-1] == '.':
                        dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i-1][j]
                elif p[i-1] == '*':
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] if p[i-1] == s[j-1] or p[i-1] == '.' else False
        return dp[sizep][sizes]
        
