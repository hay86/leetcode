class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        l = len(s)
        stack = ['']
        while i < l:
            if s[i].isdigit() and stack[-1].isdigit():
                stack[-1] += s[i]
            elif s[i].isalpha() and stack[-1].isalpha():
                stack[-1] += s[i]
            elif s[i] == ']':
                ss = stack.pop()
                stack.pop()
                ss *= int(stack.pop())
                if stack[-1].isalpha():
                    stack[-1] += ss
                else:
                    stack.append(ss)
            else:
                stack.append(s[i])
            i += 1
        return stack.pop()
