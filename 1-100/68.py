class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        size = len(words)
        if size == 0:
            return []
        w, s, ret = [0], [], []
        i, j = 1, len(words[0])
        while i < size:
            if j + len(words[i]) + 1 <= maxWidth:
                j += len(words[i]) + 1
                w.append(i)
                s.append(1)
            else:
                n = len(s)
                word = words[w[0]]
                for k in range(n):
                    d = (maxWidth-j)/(n-k) if (maxWidth-j)%(n-k) == 0 else (maxWidth-j)/(n-k) + 1
                    s[k] += d
                    j += d
                    word += ' '*s[k] + words[w[k+1]]
                if len(word) == maxWidth:
                    ret.append(word)
                else:
                    ret.append(word + ' '*(maxWidth-len(word)))
                j = len(words[i])
                w = [i]
                s = []
            i += 1
        word = ' '.join([words[x] for x in w])
        if len(word) < maxWidth:
            word += ' '*(maxWidth-len(word))
        ret.append(word)
        return ret
