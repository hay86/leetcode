class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = [0]*26
        f = [False]*26
        a = ord('a')
        for ch in s:
            d[ord(ch)-a] += 1
        stack = []
        for ch in s:
            tmp1 = ord(ch)-a
            if f[tmp1]:
                d[tmp1] -= 1
                continue
            while len(stack) > 0 and stack[-1] >= tmp1 and d[stack[-1]] > 1: 
                tmp2 = stack.pop()
                d[tmp2] -= 1
                f[tmp2] = False
            stack.append(tmp1)
            f[tmp1] = True
        return ''.join([chr(x+a) for x in stack])
