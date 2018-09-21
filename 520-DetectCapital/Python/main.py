class Solution:
    def detectCapitalUse2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # we assume non empty word so no need to check len(word)        
        return (word.upper() == word) or (word[1:].lower() == word[1:])
    
    def detectCapitalUse(self, word):
        # True if First is capitalize, False otherwise       
        prev_version = int(word[0].upper() == word[0])
        
        for i, letter in enumerate(word[1:]):
            version = int(letter.upper() == letter)
            if version > prev_version or (version < prev_version and i > 0):
                return False
            prev_version = version
        
        return True