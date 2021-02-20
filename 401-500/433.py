from collections import deque
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        visit = set([start])
        que = deque()
        que.append((start,0))
        while len(que) > 0:
            s,c = que.popleft()
            for i in range(8):
                for x in 'ACGT':
                    y = s[:i] + x + s[i+1:]
                    if y in bank and y not in visit:
                        if y == end:
                            return c+1
                        visit.add(y)
                        que.append((y, c+1))
        return -1
