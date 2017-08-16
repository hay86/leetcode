class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        trie = {}
        for word in words:
            tmp = trie
            for w in word:
                if w not in tmp:
                    tmp[w] = {}
                tmp = tmp[w]
            tmp[0] = True
        h = len(board)
        w = len(board[0]) if h > 0 else 0
        if h == 0 or w == 0:
            return []
        ret = set()
        for i in range(w):
            for j in range(h):
                self.dfs(i, j, board, w, h, trie, ret, board[j][i])
        return list(ret)
        
    def dfs(self, i, j, board, w, h, trie, ret, word):
        if board[j][i] not in trie:
            return
        trie2 = trie[board[j][i]]
        if 0 in trie2:
            ret.add(word)
            if len(trie2) == 1:
                return
        board[j][i] = '#'
        if i+1 < w:
            self.dfs(i+1, j, board, w, h, trie2, ret, word+board[j][i+1])
        if -1 < i-1:
            self.dfs(i-1, j, board, w, h, trie2, ret, word+board[j][i-1])
        if j+1 < h:
            self.dfs(i, j+1, board, w, h, trie2, ret, word+board[j+1][i])
        if -1 < j-1:
            self.dfs(i, j-1, board, w, h, trie2, ret, word+board[j-1][i])
        board[j][i] = word[-1]
