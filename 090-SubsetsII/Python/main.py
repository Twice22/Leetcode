class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        result = []
        combinations = []
        nums.sort()
        self.size = len(nums)
        
        self.build(result, nums, combinations, 0)
        return result
    
    def build(self, result, nums, combinations, idx):
        result.append(combinations)
            
        for i in range(idx, self.size):
            if i != idx and nums[i-1] == nums[i]:
                continue
            self.build(result, nums, combinations + [nums[i]], i+1)