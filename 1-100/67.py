class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a[0] == '-':
            a = a[1:]
        if b[0] == '-':
            b = b[1:]
        return bin(int(a,2)+int(b,2))[2:]
