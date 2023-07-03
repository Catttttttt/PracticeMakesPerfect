class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        res = ""
        while len(res) < len(s):
            if not words:
                return False
            res += words.pop(0)
        return res == s
