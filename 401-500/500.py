class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        ret = []
        for w in words:
            s = set(w.lower())
            if s&s1 == s or s&s2 == s or s&s3 == s:
                ret.append(w)
        return ret
        
    
