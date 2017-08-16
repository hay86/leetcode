class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size == 0 or s[0] == '0':
            return 0
        ret = [1]*(size+1)
        for i in range(1, size):
            ret[i+1] = ret[i]
            if s[i] == '0':
                if s[i-1] > '2' or s[i-1] == '0':
                    return 0
                else:
                    ret[i+1] = ret[i-1]
            elif s[i-1] == '1' or s[i-1] == '2' and s[i] <= '6':
                ret[i+1] += ret[i-1]
        return ret[size]
