class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return self.encode(num) if num >= 0 else self.encode(0xffffffff+num+1)
    
    def encode(self, num):
        if num == 0:
            return '0'
        alpha = '0123456789abcdef'
        ret = ''
        while num > 0:
            ret = alpha[num % 16] + ret
            num /= 16
        return ret
