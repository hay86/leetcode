class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ret = []
        for i in range(num+1):
            j = num-i
            if i <= 4 and j <= 6:
                r1 = self.combinations(i, 4)
                r2 = self.combinations(j, 6)
                for h in r1:
                    if h > 11:
                        continue
                    for m in r2:
                        if m > 59:
                            continue
                        ret.append('%d:%02d' % (h, m))
        return ret
                        
    
    def combinations(self, i, n):
        if n == 1:
            return [1] if i == 1 else [0]
        if n == i:
            return [2**n-1]
        if i == 0:
            return [0]
        r1 = self.combinations(i-1, n-1)
        for j in range(len(r1)):
            r1[j] = (r1[j]<<1) + 1
        r2 = self.combinations(i, n-1)
        for j in range(len(r2)):
            r2[j] = r2[j]<<1
        return r1+r2
