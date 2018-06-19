class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        subset = []
        
        self.build(nums, 0, len(nums), result, subset)
        return result
    
    def build(self, nums, beg, end, result, subset):
        
        if beg == end:
            return
        
        for i in range(beg, end):
            subset.append(nums[i])
            result.append(subset.copy())
            self.build(nums, i + 1, end, result, subset)
            subset.pop()