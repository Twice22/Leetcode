class Solution:
    def numDecodings2(self, s):
        # transform numDecodings2 to DP
        if not s:
            return 0
        
        # dp[1] = 1 means if one digit -> one solution
        dp = [1, 1]
        for i, digit in enumerate(s):
            num = 0
            if digit != "0":
                num += dp[-1]
            if i >= 1 and 10 <= int(s[i-1:i+1]) <= 26:
                num += dp[-2]
            if not num:
                return 0
            dp.append(num)
        
        return dp[-1]
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # idea on an example:
        # numDecodign(15245) -> numDecoding(1524) + numDecoding(152)
        # (1 if 10 <= 45 <= 26 else 0)
        return self.numDecodingRec(s, {})
    
    # Note: if we factorize if/elif/else... TLE so keep it this way
    def numDecodingRec(self, s, registered):
        if s in registered:
            return registered[s]
        if s == "0":
            return 0
        if not s:
            return 1
        if len(s) == 1:
            return 1
        else:
            s_1, digit = s[:-1], s[-1]
            s_2, num = s[:-2], s[-2:]
            if 10 <= int(num) <= 26 and digit != "0":
                res = self.numDecodingRec(s_1, registered) + self.numDecodingRec(s_2, registered)
            elif 10 <= int(num) <= 26 and digit == "0":
                res = self.numDecodingRec(s_2, registered)
            elif not(10 <= int(num) <= 26) and digit != "0":
                res = self.numDecodingRec(s_1, registered)
            else:
                return 0
            registered[s] = res
            return res
        