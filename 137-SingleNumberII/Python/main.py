class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # now... the elements appears 3 times. Again we can solve
        # this problem easily using extra memory (dictionary). Let's just
        # find out if we can do better...
        
        # the idea is to cancel out 3 but here if we do x ^ x ^ x we get x...
        # and not 0. So let's think about it a bit more. Let's suppose
        # the array is sorted (for conveniency). So suppose we have:
        # [n1, n1, n1, n2, n3, n3, n3, n4, n4, n4, ...]
        
        # Now let's suppos x1 is the rightmost bit of n1
        # x2 is the rightmost bit of n2, and so on
        
        # then we have: 3 * (x1 + x3 + x4) + x2. But xi can either be 0 or 1
        # so we have (3 * (x1 + x3 + x4) + x2) % 3 = x2
        # then we shift the bit and we do the same trick...
        
        result = 0
        for i in range(32):

            summ = 0
            x = (1 << i) # get bit in i-th position
            for n in nums:
                if x & n:
                    summ += 1

            result |= (summ % 3) * x

        return result if result < 2**31 else (result - (1 << 32))