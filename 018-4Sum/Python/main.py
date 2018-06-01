class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        if len(nums) < 4:
            return []
        
        nums.sort()
        size = len(nums)
        solutions = set()
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        print(nums)
        
        for i, n in enumerate(nums[:-3]):
            if i > 0 and n == nums[i-1]:
                continue
                       
            d[n] -= 1
            
            for beg in range(i+1, size):
                d[nums[beg]] -= 1
                for end in range(beg+1, size):
                    d[nums[end]] -= 1


                    if target-n-nums[beg]-nums[end] in d and d[target-n-nums[beg]-nums[end]] > 0:
                        solutions.add(tuple(sorted([n, nums[beg], target-n-nums[beg]-nums[end], nums[end]])))

                    d[nums[end]] += 1
                        
                d[nums[beg]] += 1

            d[n] += 1
                    
        return sorted(list(solutions))