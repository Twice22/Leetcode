class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        largest_sum = nums[0]
        current_largest_sum = nums[0]
        for n in nums[1:]:
            current_largest_sum = max(current_largest_sum + n, n)
            largest_sum = max(current_largest_sum, largest_sum)
        
        return largest_sum