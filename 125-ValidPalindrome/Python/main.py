class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def helper(ch):
            return "0" <= ch <= "9" or "a" <= ch <= "z" or "A" <= ch <= "Z"
        
        i, j = 0, len(s) - 1
        while i <= j:
            while i < j and not helper(s[i]): i += 1 # can use isalnum()
            while j > i and not helper(s[j]): j -= 1 # can use isalnum()

            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return i > j
        