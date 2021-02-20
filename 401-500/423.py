class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        seq = [(0,'zero'),(2,'two'),(4,'four'),(6,'six'),(8,'eight'),(1,'one'),(3,'three'),(5,'five'),(7,'seven'),(9,'nine')]
        ret = [0]*10
        c = [0]*26
        d = ord('a')
        for ss in s:
            c[ord(ss)-d] += 1
        for i,word in seq:
            minus = min(c[ord(w)-d] for w in word)
            ret[i] += minus
            for w in word:
                c[ord(w)-d] -= minus
        ans = ''
        for i in range(10):
            if ret[i] > 0:
                ans += str(i)*ret[i]
        return ans
        
