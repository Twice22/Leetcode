class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        
        result = []
        combi = []
        candidates.sort()
        
        self.kernel(result, combi, candidates, target)
        
        return result
    
    def kernel(self, result, combi, candidates, target):
        if target == 0:
            result.append(combi)
            return
        
        for i, candidate in enumerate(candidates):
            if candidate > target:
                break
            if i > 0 and candidate == candidates[i-1]:
                continue
            self.kernel(result, combi + [candidate], candidates[i+1:], target - candidate)