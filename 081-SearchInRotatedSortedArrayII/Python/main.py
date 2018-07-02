class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        beg, end, mid = 0, len(nums)-1, 0
        
        while beg <= end:
            mid = (beg + end) // 2

            if nums[mid] == target:
                return True
            elif nums[mid] == nums[beg]:
                beg += 1 
            elif (nums[beg] <= nums[mid] and nums[mid] > target >= nums[beg]) or \
               (nums[mid] <= nums[beg] and not (nums[mid] < target <= nums[end])):
                end = mid-1
            else:
                beg = mid+1

        return nums[mid] == target