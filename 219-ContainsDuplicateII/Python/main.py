class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False
        
        d = {}
        booleans = {}
        for i, n in enumerate(nums):
            if n in d and abs(d[n] - i) > k:
                if n not in booleans or (n not in booleans and not booleans[n]):
                    booleans[n] = False
                d[n] = i
            elif n in d:
                booleans[n] = True
            
            d[n] = i
        
        if not booleans:
            return False
        
        return all([v for v in booleans.values()])