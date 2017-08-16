class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        arr = []
        d = 0
        for ch in input:
            if ch in ['+','-','*']:
                arr.append(d)
                arr.append(ch)
                d = 0
            else:
                d = d*10 + int(ch)
        arr.append(d)
        return self.compute(arr)
        
    def compute(self, arr):
        n = (len(arr)+1)/2
        if n == 1:
            return [arr[0]]
        else:
            ret = []
            for i in range(1, n):
                a = self.compute(arr[0:2*i-1])
                b = self.compute(arr[2*i:])
                for aa in a:
                    for bb in b:
                        if arr[2*i-1] == '+':
                            ret.append(aa+bb)
                        elif arr[2*i-1] == '-':
                            ret.append(aa-bb)
                        elif arr[2*i-1] == '*':
                            ret.append(aa*bb)
            return ret
