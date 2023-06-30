class Solution(object):
    def isCircularSentence(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if i == len(words)-1:
                if words[i][-1] == words[0][0]:
                    return True
                else:
                    return False
            if word[-1] != words[i+1][0]:
                return False
