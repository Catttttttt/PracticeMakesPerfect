class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        dictset = set(dictionary)
        words = sentence.split(" ")
        for index, word in enumerate(words):
            for j in range(1, len(word)+1):
                if word[:j] in dictset:
                    words[index] = word[:j]
                    break
        return " ".join(words)
