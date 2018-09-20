class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        # length of chain without dashes
        length = len(S)
        true_len = length - S.count("-")
        
        if not true_len:
            return ""
        
        up = S.upper()
        
        size = (true_len % K) or K
        
        res = ""
        for i, letter in enumerate(up):
            if letter != '-':
                res += letter
                size -= 1
                
                if size == 0:
                    size = K
                    res += "-"
        
        return res[:-1] if res[-1] == '-' else res