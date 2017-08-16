class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        import random
        random.shuffle(strs)
        set1 = set()
        prefix = ''
        for i in range(len(strs)):
            set2 = set()
            prefix = ''
            for j in range(len(strs[i])):
                tmp = strs[i][:j+1]
                if i == 0 or tmp in set1:
                    set2.add(tmp)
                    prefix = tmp
                else:
                    break
            set1 = set2
            if len(set1) == 0:
                break
        return prefix
