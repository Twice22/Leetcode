class Solution:
    def binary_left(self, nums, target):
        beg, end = 0, len(nums)-1

        left = float("inf")

        while beg <= end:
            mid = (beg + end) // 2
            if target <= nums[mid]:
                if target == nums[mid]:
                    left = min(left, mid)
                end = mid-1
            else:
                beg = mid+1

        return left if left <= len(nums) else -1

    def binary_right(self, nums, target):
        beg, end = 0, len(nums)-1

        right = -1

        while beg <= end:
            mid = (beg + end) // 2
            if target < nums[mid]:
                end = mid-1
            else:
                if target == nums[mid]:
                    right = max(right, mid)
                beg = mid+1

        return right
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binary_left(nums, target)
        if left == -1:
            return [-1, -1]
        right = self.binary_right(nums, target)
        return [left, right]