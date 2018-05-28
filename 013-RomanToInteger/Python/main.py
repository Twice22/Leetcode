class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X":10, "V": 5, "I":1, "@": 0}
        
        res = 0
        prev_l = "@"
        for l in s:
            res += d[l] - 2 * d[prev_l] if d[prev_l] < d[l] else d[l]
            prev_l = l
            
        return res