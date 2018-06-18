class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # need a one-pass algorithm using only constant space?
        # no worry Billy!
        
        p0, p2 = 0, len(nums) - 1
        idx = 0
        
        while idx <= p2:
            if nums[idx] == 0:
                nums[p0], nums[idx] = 0, nums[p0]
                p0 += 1
            
            if nums[idx] == 2:
                nums[p2], nums[idx] = 2, nums[p2]
                p2 -= 1
                
                # need to decrement here because we
                # can have a 2 at p2 and a 2 at idx
                # if we don't decrement at the next iteration
                # we would have a 2 in the middle of 0 or 1...
                idx -= 1
            
            idx += 1