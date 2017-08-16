class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for s in tokens:
            if s == '+':
                stack.append(stack.pop() + stack.pop())
            elif s == '-':
                v = stack.pop()
                stack.append(stack.pop() - v)
            elif s == '*':
                stack.append(stack.pop() * stack.pop())
            elif s == '/':
                v = stack.pop()
                u = stack.pop()
                if u < 0 and v > 0:
                    stack.append(-(-u / v))
                elif u > 0 and v < 0:
                    stack.append(-(u / -v))
                else:
                    stack.append(u / v)
            else:
                stack.append(int(s))
        return stack[0]
