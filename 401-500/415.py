class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ret = []
        i, carry = -1, 0
        while i >= -min(len(num1), len(num2)):
            tmp = int(num1[i])+int(num2[i])+carry
            ret.append(str(tmp%10))
            carry = tmp/10
            i -= 1
        while i >= -len(num1):
            tmp = int(num1[i])+carry
            ret.append(str(tmp%10))
            carry = tmp/10
            i -= 1
        while i >= -len(num2):
            tmp = int(num2[i])+carry
            ret.append(str(tmp%10))
            carry = tmp/10
            i -= 1
        if carry > 0:
            ret.append('1')
        return ''.join(ret[::-1])
            
