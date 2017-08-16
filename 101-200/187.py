class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        size = len(s)
        ret, st = set(), set()
        for i in range(size-9):
            v = s[i:i+10]
            if v in st:
                ret.add(v)
            else:
                st.add(v)
        return list(ret)
