class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        
        
        nums.sort()
        size = len(nums)-1
        diff = float("inf")
        best_sum = 0
        
        for i, n in enumerate(nums[:-2]):
            if i > 0 and n == nums[i-1]:
                continue
            
            beg, end = i+1, size
            
            while beg < end:
                total = n + nums[beg] + nums[end]
                temp_diff = abs(target - total)
                
                if not temp_diff:
                    return total
                
                if temp_diff < diff:
                    diff = temp_diff
                    best_sum = total
                
                if total < target:
                    beg += 1
                else:
                    end -= 1
            
        return best_sum