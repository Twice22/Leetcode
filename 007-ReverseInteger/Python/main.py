class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        
        n = 0
        while x:
            n = (x % 10) + n * 10
            x //= 10
        
        if n > (2**31):
            return 0
        
        return n