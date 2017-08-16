class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.ret =set()
        self.dfs(num, [], target)
        return list(self.ret)
        
    def dfs(self, num, arr, target):
        size = len(num)
        if size == 0:
            if len(arr) > 0:
                self.cal(arr, target, '', False)
        else:
            for i in range(1, size+1):
                if num[0] != '0' or i == 1:
                    arr.append(int(num[:i]))
                    self.dfs(num[i:], arr, target)
                    arr.pop()
            
    def cal(self, arr, target, exp, reverse):
        size = len(arr)
        if size == 0 and target == 0:
            self.ret.add(exp)
        else:
            val = arr[0]
            exp += str(val)
            plus, minus = ('+','-') if not reverse else ('-','+')
            for i in range(1,size):
                a, b = arr[i], arr[i:]
                self.cal(b, target-val, exp+plus, reverse)
                self.cal(b, -target+val, exp+minus, not reverse)
                val *= a
                exp += ('*'+str(a))
            if val == target:
                self.ret.add(exp)
            
            
