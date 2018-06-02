class Solution:    
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        n, x_bis = 0, x
        while x_bis:
            r = x_bis % 10
            x_bis = x_bis // 10
            n = n * 10 + r
        
        return x == n
    
    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        l = str(x)
        size = len(l) // 2
        i = 0
        
        while i <= size and l[i] == l[-(i+1)]:
            i += 1
        
        return (i >= size)
    
    def isPalindrome3(self, x):
        l = str(x)
        return l == l[::-1]