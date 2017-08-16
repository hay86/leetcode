from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        
        for k in c1:
            if c1[k] > c2[k]:
                return False
        return True
