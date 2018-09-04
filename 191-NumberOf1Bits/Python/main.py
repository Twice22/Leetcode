class Solution(object):
    # O(len(n)) solution (not the best!)
    def hammingWeight2(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            c += n & 1
            n = n >> 1

        return c
    
    # O(log(n)) solution. Here we go!
    def hammingWeight3(self, n):
        c = 0
        while n:
            c += 1
            n &= (n-1)

        return c
    
    def hammingWeight(self, n):
        return bin(n).count('1')