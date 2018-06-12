class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        str = s.strip()
        
        for i, l in enumerate(reversed(str)):
            if l == ' ':
                return i
        
        return len(str)