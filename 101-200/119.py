class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        ret = [1]
        for i in range(1, rowIndex+1):
            for j in range(i-1):
                ret.append(ret.pop(0)+ret[0])
            ret.append(1)
        return ret
