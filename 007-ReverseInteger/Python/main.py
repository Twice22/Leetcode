class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # handle negative numbers
        sgn = True if x < 0 else False
        x = x if x > 0 else -x
        
        l = []
        while x != 0:
            l.append(x % 10)
            x = x // 10
        
        size = len(l)-1
        r = sum([10**(size-i)*e for i, e in enumerate(l)])
        
        if r > 2**31:
            return 0
        return -r if sgn else r