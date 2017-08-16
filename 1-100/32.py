class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        if size == 0:
            return 0
        stack = []
        for i in range(size):
            if len(stack) > 0 and s[stack[-1]] == '(' and s[i] == ')':
                stack.pop()
            else:
                stack.append(i)
        stack.append(size)
        start = 0
        ret = 0
        for i in stack:
            if i-start > ret:
                ret = i-start
            start = i+1
        return ret
