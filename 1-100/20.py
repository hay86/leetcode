class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        arr = []
        for x in s:
            if x=='(' or x=='{' or x=='[':
                arr.append(x)
            elif len(arr) > 0:
                if x==')' and arr[-1] == '(':
                    arr.pop()
                elif x=='}' and arr[-1] == '{':
                    arr.pop()
                elif x==']' and arr[-1] == '[':
                    arr.pop()
                else:
                    return False
            else:
                return False
        return len(arr) == 0
