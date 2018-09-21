class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "0"
        
        n = abs(num)
        
        res = ""
        while n:
            res = str(n % 7) + res
            n = n // 7
        
        return "-"*(num < 0) + res