class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        size = len(nums)
        maxi = 0
        
        # replace negative number by 0
        for i in range(size):
            maxi = max(maxi, nums[i])
            if nums[i] < 0 or nums[i] >= size:
                nums[i] = 0
               
        for i in range(size):
            ptr = i
            already_looped = False
            while 0 < nums[ptr] < size:
                temp = nums[ptr] if already_looped else nums[nums[ptr]]
                if not already_looped:
                    nums[nums[ptr]] = -1
                else:
                    if ptr >= 0:
                        nums[ptr] = -1
                if ptr >= 0:
                    ptr = temp
                else:
                    break
                already_looped = True
            if already_looped and ptr > 0:
                nums[ptr] = -1

        
        for i, n in enumerate(nums[1:]):
            if n != -1:
                return (i+1)
        
        return len(nums) + (1 if maxi == size else 0)