class Solution:
    def productExceptSelf2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = [1] * size
        prod = 1
        for i in range(1, size):
            res[i] *= prod
            prod *= nums[i]
        
        prod = 1
        for j in range(size-1, -1, -1):
            res[j] *= prod
            prod *= nums[j]
        
        return res
    
    def productExceptSelf(self, nums):
        size = len(nums)
        res = [1] * size
        left, right = 1, 1
        for i in range(size):
            res[i] *= left
            res[size-i-1] *= right
            left *= nums[i]
            right *= nums[size-i-1]
        
        return res