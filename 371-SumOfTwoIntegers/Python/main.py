class Solution:
    # this solution does not work due to infinite bit representation
    # in Python...
    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # c is the carry   
        # the total is solely a + b + c
        # which is nothing else then a ^ b ^ c + handle the final carry... 
        while b:
            c = (a & b) << 1
            a = a ^ b
            b = c

        return a
    
    # corrected version for Python and infinite bit representation
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # to limitate the infinite bit representation in python, we can use
        # a mask with all bit to 1 : 0xFFFFFFFF
        mask = 0xFFFFFFFF
        while b:
            c = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = c

        # the problem with this mask trick is that Python
        # loose the track of the sign bit. Hence python does
        # not know if the resulting number should be positive
        # or negative. To correct this we just have to say that
        # if a >= 2^31 = 1 << 31 then is is actually a negative number
        # otherwise we return a. To get the negative number associated
        # with a >= 2^31 we just need to get the 2-complement representation
        # of this number that is to say ~(a ^ mask)
            
        return a if a < (1 << 31) else ~(a ^ mask)