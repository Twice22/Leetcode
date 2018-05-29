class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # classic trick, go reverse way to
        # avoid deleting element while iterating
        # on the list...
        
        temp = -1 # last element
        for n in reversed(nums[:-1]):
            if n == nums[temp]:
                del nums[temp]
            else:
                temp -= 1
            
        return len(nums)