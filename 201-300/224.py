class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.strip() == '':
            return 0
        tokens, ops = [], []
        val, flag = 0, False
        for ss in s:
            if '0' <= ss <= '9':
                val = val*10+int(ss)
                flag = True
            else:
                if flag:
                    tokens.append(val)
                    val, flag = 0, False
                if ss == '+' or ss == '-':
                    if len(ops) > 0 and ops[-1] != '(':
                        tokens.append(ops.pop())
                    ops.append(ss)
                elif ss == '(':
                    ops.append(ss)
                elif ss == ')':
                    while len(ops) > 0 and ops[-1] != '(':
                        tokens.append(ops.pop())
                    if len(ops) > 0:
                        ops.pop()
        if flag:
            tokens.append(val)
        while len(ops) > 0 and ops[-1] != '(':
            tokens.append(ops.pop())
        stack = []
        for s in tokens:
            if s == '+':
                stack.append(stack.pop() + stack.pop())
            elif s == '-':
                v = stack.pop()
                stack.append(stack.pop() - v)
            else:
                stack.append(int(s))
        return stack[0]
