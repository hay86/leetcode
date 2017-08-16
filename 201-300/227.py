class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, op = [], []
        val = 0
        for ss in s:
            if '0' <= ss <= '9':
                val = val*10 + int(ss)
            elif ss == '+':
                if len(op) == 0:
                    ret.append(val)
                else:
                    while len(op) > 0:
                        val = self.do_cal(ret.pop(), val, op.pop())
                    ret.append(val)
                op.append(ss)
                val = 0
            elif ss == '-':
                if len(op) == 0:
                    ret.append(val)
                else:
                    while len(op) > 0:
                        val = self.do_cal(ret.pop(), val, op.pop())
                    ret.append(val)
                op.append(ss)
                val = 0
            elif ss == '*':
                if len(op) == 0 or op[-1] == '+' or op[-1] == '-':
                    ret.append(val)
                else:
                    ret.append(self.do_cal(ret.pop(), val, op.pop()))
                op.append(ss)
                val = 0
            elif ss == '/':
                if len(op) == 0 or op[-1] == '+' or op[-1] == '-':
                    ret.append(val)
                else:
                    ret.append(self.do_cal(ret.pop(), val, op.pop()))
                op.append(ss)
                val = 0
        while len(op) > 0:
            val = self.do_cal(ret.pop(), val, op.pop())
        return val
    
    def do_cal(self, a, b, op):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        else:
            return int(a/b)
        
