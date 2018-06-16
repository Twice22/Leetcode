class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """       
        beg, end = 0, x
        while True:
            mid = ((beg + end) // 2)
            if mid*mid <= x < (mid+1)*(mid+1):
                return mid
            
            if mid*mid < x:
                beg = mid+1
            else:
                end = mid-1

        
        return 1