class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        size = len(num)
        for i in range(size-1):
            for j in range(i+1, size):
                if num[0] == '0' and i > 0:
                    continue
                if num[i+1] == '0' and j-i > 1:
                    continue
                a, b = int(num[:i+1]), int(num[i+1:j+1])
                c, s = a+b, j+1
                l, t = len(str(c)), 0
                while s < size and s+l <= size and (num[s] != '0' or l==1) and c == int(num[s:s+l]):
                    a, b = b, c
                    c, s = a+b, s+l
                    l = len(str(c))
                    t += 1
                if s == size and t > 0:
                    return True
        return False
                
