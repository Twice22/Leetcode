class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        beg_idx = 0
        end_idx = 0
        
        size = len(s)-1
        max_len = 1
        
        
        for i, letter in enumerate(s):
            
            r_idx = l_idx = i
            
            # odd palindrome
            while 0 < l_idx and r_idx < size and s[l_idx-1] == s[r_idx+1]:
                l_idx -= 1
                r_idx += 1
            
            if r_idx - l_idx > end_idx - beg_idx:
                beg_idx, end_idx = l_idx, r_idx
                
            # even palindrome
            if i > 0 and s[i-1] == s[i]:
                r_idx, l_idx = i, i-1
                while 0 < l_idx and r_idx < size and s[l_idx-1] == s[r_idx+1]:
                    l_idx -= 1
                    r_idx += 1
                
                if r_idx - l_idx > end_idx - beg_idx:
                    beg_idx, end_idx = l_idx, r_idx 
                
        
        return s[beg_idx: end_idx+1]
            