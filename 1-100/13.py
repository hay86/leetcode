class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'i':1,'I':1,'v':5,'V':5,'x':10,'X':10,'l':50,'L':50,'c':100,'C':100,'d':500,'D':500,'m':1000,'M':1000}
        sum = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and dict[s[i]] < dict[s[i+1]]:
                sum += dict[s[i+1]] - dict[s[i]]
                i += 1
            else:
                sum += dict[s[i]]
            i += 1
        return sum
