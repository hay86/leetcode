from collections import deque
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1 = [0]*256
        s2 = [0]*256
        for ch in t:
            i = ord(ch)
            s1[i] += 1
        total = 0
        for i in range(256):
            if s1[i] > 0:
                total += 1
        size = len(s)
        que = deque()
        x, y = -1, 2147483647
        for i in range(size):
            j = ord(s[i])
            if s1[j] > 0:
                s2[j] += 1
                if s2[j] == s1[j]:
                    total -= 1
                que.append(i)
                k = ord(s[que[0]])
                while s2[k] > s1[k]:
                    que.popleft()
                    s2[k] -= 1
                    k = ord(s[que[0]])
                if total == 0:
                    diff = que[-1] - que[0]
                    if diff < y:
                        x, y = que[0], diff
        return s[x:x+y+1] if x > -1 else ''
        
