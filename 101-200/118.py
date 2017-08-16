class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            ret = []
        else:
            ret = [[1]]
            for i in range(1, numRows):
                tmp = [1]
                for j in range(len(ret[-1])-1):
                    tmp.append(ret[-1][j]+ret[-1][j+1])
                tmp.append(1)
                ret.append(tmp)
        return ret
