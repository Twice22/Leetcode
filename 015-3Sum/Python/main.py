class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        solutions = set()
        nums.sort()
        
        for i, n in enumerate(nums[:-2]):
            # if sequence of same numbers
            # don't do anything because we have
            # already done something with the first
            # number different from the previous
            if i > 0 and n == nums[i-1]:
                continue
            
            # create a dictionary
            d = {}
            
            # iterate over the other numbers (o_n)
            for o_n in nums[i+1:]:
                if o_n in d:
                    solutions.add((n, -o_n-n, o_n))
                else:
                    d[-o_n-n] = True
        
        return list(solutions)