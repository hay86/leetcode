class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        ret = 0
        while n > 0:
            strn = str(n)
            size = len(strn)
            if size > 1:
                ret += (size-1)*10**(size-2)
                if strn[0] == '1':
                    ret += int(strn[1:])+1
                    n = int(strn[1:])
                else:
                    ret += (10**(size-1)+(int(strn[0])-1)*(size-1)*10**(size-2))
                    n = int(strn[1:])
            elif n > 0:
                ret += 1
                n = 0
        return ret
                
