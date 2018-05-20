class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {target-nums[i]: i for i in range(len(nums))}
        for i, n in enumerate(nums):
            if n in d and d[n] != i:
                return [i, d[n]]
        
        return None