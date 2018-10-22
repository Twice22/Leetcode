class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0:
            return False
        
        d = {}
        for i, n in enumerate(nums):
            idx = n // (t+1)
            for x in range(idx-1, idx+1+1):
                print(idx, x, n)
                if x in d and abs(d[x] - n) <= t:
                    return True
            
            d[idx] = n
            if len(d) > k:
                del d[nums[i-k] // (t+1)]
        
        return False
        