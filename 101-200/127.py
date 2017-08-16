from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        size = len(beginWord)
        que = deque([(beginWord, 1)])
        visit = set()
        while que:
            word, deep = que.popleft()
            for i in range(size):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    w = word[:i]+j+word[i+1:]
                    if w in wordList and w not in visit:
                        if w == endWord:
                            return deep+1
                        que.append((w, deep+1))
                        visit.add(w)
        return 0
        
