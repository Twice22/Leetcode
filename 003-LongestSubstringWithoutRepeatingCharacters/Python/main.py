class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        overall_max = 0
        max_len = 0
        d = {}
        
        for idx, letter in enumerate(s):
            if letter not in d:
                max_len += 1
                
            if letter in d:
                max_len = max_len + 1 if idx - d[letter] > max_len else idx - d[letter]
            
            d[letter] = idx
            
            overall_max = max(max_len, overall_max)
            
        return overall_max