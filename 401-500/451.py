class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = set(s)
        c = [(x, s.count(x)) for x in ss]
        c.sort(key=lambda x: x[1], reverse = True)
        return ''.join([x[0]*x[1] for x in c])