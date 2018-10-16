class Solution:    
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        length = float("inf")
        size = len(nums)
        current_sum = 0
        j = 0
        
        for i in range(size):
            while j < size and current_sum < s and j-i < length:
                current_sum += nums[j]
                j += 1
            
            if current_sum >= s:
                length = min(length, j-i)
            
            if length == 1:
                break
            
            current_sum -= nums[i]
        
        return 0 if length == float("inf") else length