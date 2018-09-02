class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """        
        # 0011100110
        # 2 - switch - 3 - switch - 2 - switch - 2 - switch 1
        # res = min(2,3) + min(3,2) + min(2,2) + min(2, 1) = 7
        # Note: we assume len(s) >= 1 so we don't need to check
        # if s[0] actually exists because it does!
        c0, c1 = 1, 0
        
        prev_letter = s[0]
        res = 0
        
        for letter in s[1:]:
            if prev_letter == letter:
                c0 += 1
            else:
                res += min(c0, c1)
                c0, c1 = 1, c0
            
            prev_letter = letter
        
        return res + min(c0, c1)
            