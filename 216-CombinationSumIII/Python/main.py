class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        
        def helper(k, n, combination=[], beg=1):            
            if k == 0 and n == 0:
                res.append(combination)
                return
            
            for i in range(beg, 10):
                if n - i >= 0:
                    helper(k-1, n-i, combination + [i], i+1)
        
        helper(k, n)
        return res