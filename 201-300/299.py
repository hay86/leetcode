class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = [0]*10, [0]*10
        a, b = 0, 0
        n = len(secret)
        for i in range(n):
            if secret[i] == guess[i]:
                a += 1
            else:
                s[int(secret[i])] += 1
                g[int(guess[i])] += 1
        for i in range(10):
            b += min(s[i],g[i])
        return '%dA%dB' % (a, b)
