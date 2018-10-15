class Solution(object):
    def rangeBitwiseAnd2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if n == m:
            return n
        
        x, i = 1, -1
        diff = n - m
        res = 0
        while n:
            if not (x < diff or (n & m & 1) == 0):
                res += 2 << i
            n >>= 1
            m >>= 1
            x <<= 1
            i += 1
            
        
        return res
    
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n &= n-1
        return n