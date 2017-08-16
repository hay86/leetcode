class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        arr = preorder.split(',')
        for p in arr:
            stack.append(p)
            while len(stack) > 1 and stack[-1] == '#' and stack[-2] == '#':
                stack.pop()
                stack.pop()
                print stack
                if len(stack) > 0 and stack[-1] != '#':
                    stack[-1] = '#'
                else:
                    return False
        return len(stack) == 1 and stack[-1] == '#'
