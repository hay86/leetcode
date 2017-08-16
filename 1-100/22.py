class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        self.generate(n, n, '', ret)
        return ret
        
    def generate(self, leftL, leftR, str, ret):
        if leftL == 0 and leftR == 0:
            ret.append(str)
        if leftL > 0:
            self.generate(leftL-1, leftR, str+'(', ret)
        if leftR > 0 and leftR > leftL:
            self.generate(leftL, leftR-1, str+')', ret)
