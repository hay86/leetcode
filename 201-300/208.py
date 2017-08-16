class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = [None]*26
        self.end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root
        for w in word:
            p = ord(w) - 97
            if root.next[p] is None:
                root.next[p] = TrieNode()
            root = root.next[p]
        root.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root
        for w in word:
            p = ord(w) - 97
            if root.next[p] is None:
                return False
            root = root.next[p]
        return root.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root
        for w in prefix:
            p = ord(w) - 97
            if root.next[p] is None:
                return False
            root = root.next[p]
        return True
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
