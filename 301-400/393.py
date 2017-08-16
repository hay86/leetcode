class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        l = len(data)
        while True:
            if i >= l:
                break
            n = 0
            if data[i] & 128 == 0:
                n = 1
            elif data[i] & 224 == 192:
                n = 2
            elif data[i] & 240 == 224:
                n = 3
            elif data[i] & 248 == 240:
                n = 4
            else:
                return False
            for j in range(n-1):
                i += 1
                if i >= l or data[i] & 192 != 128:
                    return False
            i += 1
        return True
