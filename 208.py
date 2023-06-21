class Trie(object):

    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        for ch in word:
            ch = ord(ch) - ord('a')
            if not self.children[ch]:
                self.children[ch] = Trie()
            self = self.children[ch]
        self.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        for ch in word:
            ch = ord(ch) - ord('a')
            if self.children[ch]:
                self = self.children[ch]
            else:
                return False
        if self.isEnd:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if not self.children[ch]:
                return False
            else:
                self = self.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
