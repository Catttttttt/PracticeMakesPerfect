class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        """
        dictset = set(dictionary)
        words = sentence.split(" ")
        for index, word in enumerate(words):
            for j in range(1, len(word)+1):
                if word[:j] in dictset:
                    words[index] = word[:j]
                    break
        return " ".join(words)
        """
        trie = {}
        for root in dictionary:
            cur = trie
            for c in root:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur[0] = {}
        
        words = sentence.split()
        for index, word in enumerate(words):
            cur = trie
            for j, c in enumerate(word):
                if 0 in cur:
                    words[index] = word[:j]
                    break
                if c not in cur:
                    break
                cur = cur[c]
        return " ".join(words)
