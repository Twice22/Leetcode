class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # we don't care about the order...
        # well let's do it by shuffling
        if not nums:
            return 0
        
        size = len(nums)
        j = size-1
        while nums[j] == val and j >= 0:
            j -= 1

        # counter
        c = (size-1 - j) # how many val at the end of array
        
        i = 0
        while i < j:
            while i < size and nums[i] != val:
                i += 1
            
            if i >= j:
                break
                
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
            c += 1
            
            while 0 <= j and nums[j] == val:
                j -= 1
                c += 1
        
        return size - c
        