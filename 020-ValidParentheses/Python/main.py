class Solution:
    def __init__(self):
        self.d = {"(": ")", "[": "]", "{": "}"}
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """        
        if not s:
            return True
        
        pile = [s[0]]
        
        for letter in s[1:]:
            if len(pile) and pile[-1] in self.d and letter == self.d[pile[-1]]:
                del pile[-1]
            else:
                pile.append(letter)
        
        return (not pile)