class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= numRows:
            return s
        ret = [[] for i in range(numRows)]
        i, j = 0, 1
        for ss in s:
            ret[i].append(ss)
            i += j
            if i == 0 or i == numRows - 1:
                j *= -1
        return ''.join(map(lambda x: ''.join(x), ret))
