class Solution:
    def __init__(self):
        self.mapping = {i: chr(65+i) for i in range(26)}
    
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ""
        while n > 0:
            n -= 1
            s = self.mapping[n % 26] + s
            n //= 26
        
        return s
        