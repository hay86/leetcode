class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        part = path.split('/')
        stack = []
        for p in part:
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            elif p != '' and p != '.':
                stack.append(p)
        return '/'+'/'.join(stack)
