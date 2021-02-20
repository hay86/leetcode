class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            while len(stack) > 0 and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
            if k == 0:
                break
        while len(stack) > 0 and k > 0:
            stack.pop()
            k -= 1
        ret = ''.join(stack) + num[i+1:]
        for i in range(len(ret)):
            if ret[i] != '0':
                break
        ret = ret[i:]
        return '0' if ret == '' else ret
        
                
