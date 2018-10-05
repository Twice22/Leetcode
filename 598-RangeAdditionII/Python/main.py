class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # we just need to return min_x * min_y       
        return m * n if not ops else min(x[0] for x in ops) * min(y[1] for y in ops)