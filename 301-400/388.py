class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        val = input.split('\n')
        arr = [val[0]]
        ret, tmp = len(val[0]) if '.' in val[0] else 0, len(val[0])
        for i in range(1, len(val)):
            p = val[i].rfind('\t')
            p = p+1 if p >= 0 else 0
            s = val[i][p:]
            while len(arr) > p:
                v = arr.pop()
                tmp -= len(v)
            arr.append(s)
            tmp += len(s)
            if '.' in s:
                ret = max(ret, tmp+len(arr)-1)
        return ret
