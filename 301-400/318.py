class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        ret = 0
        encode = []
        for word in words:
            tmp = 0
            for ch in word:
                tmp |= (1<<(ord(ch)-97))
            encode.append(tmp)
        size = len(encode)
        for i in range(size-1):
            for j in range(i+1, size):
                if encode[i] & encode[j] == 0 and len(words[i]) * len(words[j]) > ret:
                    ret = len(words[i]) * len(words[j])
        return ret
