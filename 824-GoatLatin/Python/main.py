class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split()
        res = []
        
        for i, w in enumerate(words, 1):
            new_word = ""
            if w[0].lower() in {"a", "e", "i", "o", "u"}:
                new_word += w
            else:
                new_word += w[1:] + w[0]
            new_word += "ma" + "a" * i
            res.append(new_word)
        
        return " ".join(res)