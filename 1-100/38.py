class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return '1'
        ret = '1'
        cur = ret[0]
        num = 1
        for i in range(n-1):
            size = len(ret)
            tmp = ''
            for j in range(1,size):
                if ret[j] == cur:
                    num += 1
                else:
                    tmp += str(num)+str(cur)
                    cur = ret[j]
                    num = 1
            ret = tmp+str(num)+str(cur)
            cur = ret[0]
            num = 1
        return ret
