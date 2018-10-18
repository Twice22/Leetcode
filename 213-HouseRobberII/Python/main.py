class Solution:
    def linerob(self, nums):
        if not nums:
            return 0
        
        max_without_last, max_with_last = 0, 0
        for n in nums:
            max_without_last, max_with_last = max_with_last, max(max_without_last + n, max_with_last)
        
        return max(max_without_last, max_with_last)
            
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the house are now arranged in a circle
        # by dynamic programming if we don't have
        # a circle:
        # rob returns:
        # 1. the larger amount containing eventually the last house
        # 2. the larger amount that don't contain the last house
        
        # when there is a circle, 3 choices:
        # - we have 1. and we rob the first house -> discard this possibility
        # - we have 1. and we didn't rob the first house -> keep this possibility
        # - we have 2. -> keep this possibility 
        
        # example: [3, 2, 7, 9, 3, 18]
        # - 3 + 9 + 18 -> discard cause 3 next to 18
        # - 2 + 9 + 18 -> keep it
        # - 3 + 7 + 3 -> keep it
        # so the result is max(2+9+18, 3+7+3) = 29
        
        # so we need to apply the robber strategy on nums[1:] (first possibility)
        # and on num[:-1] or on num but we only keep the larger amount that don't contain the last house
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        return max(self.linerob(nums[1:]), self.linerob(nums[:-1]))