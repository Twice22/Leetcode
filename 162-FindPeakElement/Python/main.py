class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # this solution works because we assume
        # nums[-1] = nums[n] = -inf
        lower, upper = 0, len(nums) - 1
        while lower < upper:
            mid = (lower + upper) // 2
            if nums[mid] < nums[mid+1]:
                lower = mid + 1
            else:
                upper = mid
        
        return lower