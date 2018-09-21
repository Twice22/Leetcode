class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        d = {value: idx for idx, value in enumerate(sorted(nums, reverse=True))}
        
        txt = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, n in enumerate(nums):
            nums[i] = txt[d[n]] if d[n] < 3 else str(d[n]+1)
        
        return nums