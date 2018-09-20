class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # based on the explanations given here:
        # https://leetcode.com/problems/largest-palindrome-product/discuss/96294/Could-any-python-experts-share-their-codes-within-100ms/100809
        
        if n == 1: return 9
        
        power = 10**n
        
        # a = i + j
        for a in range(2, 9 * power // 10):
            upper = power - a
            lower = int(str(upper)[::-1])
            
            # solve for i: lower == a * i - i * i
            delta = a**2 - 4 * lower
            
            # if real solutions exist
            if delta >= 0:
                root = math.sqrt(delta)
                i1, i2 = (a - root) / 2, (a + root) / 2

                # i1, i2 > 0, just need to check they are
                # integers. If so return
                if abs(i1 - int(i1)) < 10e-6 or abs(i2 - int(i2)) < 10e-6:
                    return (upper * power + lower) % 1337
                    