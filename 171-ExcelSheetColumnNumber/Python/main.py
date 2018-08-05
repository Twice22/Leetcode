class Solution(object):
    def __init__(self):
        self.mapping = {chr(64+i): i for i in range(1, 27)}
    
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        for i, l in enumerate(reversed(s)):
            r += (26**i) * self.mapping[l]
        
        return r
        