class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # idea on an example:
        # numDecodign(15245) -> numDecoding(1524) + 1 (5)
        # + numDecoding(152) + (1 if 45 < 26 else 0)
        return self.numDecodingRec(s, {})
        
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
        