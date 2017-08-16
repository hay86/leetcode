class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            k = ''.join(sorted(list(s)))
            if k not in m:
                m[k] = [s]
            else:
                m[k].append(s)
        ret = []
        for k,v in m.items():
            v.sort()
            ret.append(v)
        return ret
