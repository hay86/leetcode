class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []
        m = [' ','*','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        ret = []
        self.comb(digits, 0, [], ret, m)
        return ret
        
    def comb(self, digits, i, path, ret, m):
        if i == len(digits):
            ret.append(''.join(path))
            return
        d = int(digits[i])
        for ch in m[d]:
            path.append(ch)
            self.comb(digits, i+1, path, ret, m)
            path.pop()
