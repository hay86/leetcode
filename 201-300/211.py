class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.next = [None]*26
        self.end = False

class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root
        for w in word:
            p = ord(w) - 97
            if not root.next[p]:
                root.next[p] = TrieNode()
            root = root.next[p]
        root.end = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.do_search(word, 0, self.root)
        
    def do_search(self, word, i, root):
        if i > len(word) or not root:
            return False
        elif i == len(word):
            return root.end
        elif word[i] == '.':
            for child in root.next:
                if child and self.do_search(word, i+1, child):
                    return True
            return False
        else:
            p = ord(word[i]) - 97
            if not root.next[p]:
                return False
            return self.do_search(word, i+1, root.next[p])

# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
