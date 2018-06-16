class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # by DP we notice it is nothing but the fibonacci series
        
        res_pp, res_p = 0, 1
        for i in range(n):
            res_pp, res_p = res_p, res_pp + res_p
        
        return res_p