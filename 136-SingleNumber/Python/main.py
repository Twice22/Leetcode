class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # obviously one can solve this problem easily with a dictionary but then
        # we would need to use extra memory. One trick we can thing off is that
        # 2 numbers can cancel out if we use a xor operation and so in the end
        # if we xor all the array we get the only number that appears once!
        
        # the array is suppose non empty so no need to check "if not nums:"
        res = nums[0]
        
        for n in nums[1:]:
            res ^= n
        
        return res