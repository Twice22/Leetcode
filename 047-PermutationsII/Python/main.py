class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        result = []

        self.permuteUniqueRec(result, nums, 0)

        return result

    def permuteUniqueRec(self, result, nums, beg):

        if beg == len(nums):
            result.append(nums.copy())
            return

        for i in range(beg, len(nums)):
            if self.alreadySeen(nums, beg, i):
                nums[beg], nums[i] = nums[i], nums[beg]
                self.permuteUniqueRec(result, nums, beg+1)
                nums[beg], nums[i] = nums[i], nums[beg]
    
    def alreadySeen(self, nums, beg, end):
        for i in range(beg, end):
            if nums[i] == nums[end]:
                return False
        return True