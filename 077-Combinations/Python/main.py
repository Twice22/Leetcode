class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        combi = []
        
        self.build(n, k, result, combi, 1)
        
        return result
    
    def build(self, n, k, result, combi, beg):
        if k == 0:
            result.append(combi)
            return
        
        for i in range(beg, n+1):
            self.build(n, k-1, result, combi + [i], beg=i+1)
